from flask import Blueprint, render_template, flash
from .forms import SignForm, VerifyForm
from bitcoin_message_tool import bmt

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@views.route('/sign', methods=['GET', 'POST'])
def sign_page():
    sign_form = SignForm()
    if sign_form.validate_on_submit():
        try:
            signed = bmt.sign_message(
                sign_form.private_key.data,
                sign_form.address_type.data,
                sign_form.message.data,
                deterministic=sign_form.deterministic.data,
                electrum=sign_form.electrum.data,
            )
        except bmt.PrivateKeyError as err:
            flash(f'Private key is invalid: {err}', 'danger')
        except bmt.SignatureError as err:
            flash(f'Signature is invalid: {err}', 'danger')
        except bmt.PointError as err:
            flash(f'Point is invalid: {err}', 'danger')
        else:
            flash("Message is signed succesfully!", 'success')
            return render_template('sign.html', form=sign_form, sig=signed)
    if sign_form.errors:
        for err_msg in sign_form.errors.values():
            flash(f'There was an error with creating a user: {err_msg[0]}', 'danger')

    return render_template('sign.html', form=sign_form, sig=None)


@views.route('/verify', methods=['GET', 'POST'])
def verify_page():
    verify_form = VerifyForm()
    if verify_form.validate_on_submit():
        try:
            verified, pubkey, result = bmt.verify_message(
                verify_form.address.data,
                verify_form.message.data,
                verify_form.signature.data,
                electrum=verify_form.electrum.data,
            )
        except bmt.PrivateKeyError as err:
            flash(f'Private key is invalid: {err}', 'danger')
        except bmt.SignatureError as err:
            flash(f'Signature is invalid: {err}', 'danger')
        except bmt.PointError as err:
            flash(f'Point is invalid: {err}', 'danger')
        else:
            if verified:
                flash(result, 'success')
            else:
                flash(result, 'danger')
            return render_template('verify.html', form=verify_form)
    if verify_form.errors:
        for err_msg in verify_form.errors.values():
            flash(f'There was an error with creating a user: {err_msg[0]}', 'danger')

    return render_template('verify.html', form=verify_form)
