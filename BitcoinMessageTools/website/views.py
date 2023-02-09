from flask import Blueprint, render_template, flash, redirect, request, url_for
from .forms import SignForm, VerifyForm
from bitcoin_message_tool import bmt

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@views.route('/sign', methods=['GET', 'POST'])
def sign_page():
    sign_form = SignForm()
    if request.method == "POST":
        try:
            address, _, signature = bmt.sign_message(
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
            flash(f"Message is signed succesfully with address: {address}", 'success')
            sign_form.signature.data = signature
    return render_template('sign.html', form=sign_form)


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
