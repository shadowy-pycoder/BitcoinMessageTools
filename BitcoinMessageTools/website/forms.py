from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, PasswordField, BooleanField, TextAreaField
from wtforms.validators import DataRequired


class SignForm(FlaskForm):

    private_key = PasswordField(
        label='Private Key',
        validators=[DataRequired()],
    )
    address_type = SelectField(
        label='Address Type',
        validators=[DataRequired()],
        choices=[('p2pkh', 'P2PKH'), ('p2wpkh-p2sh', 'P2WPKH-P2SH'), ('p2wpkh', 'P2WPKH')]
    )
    message = TextAreaField(
        label='Message',
        validators=[DataRequired()],
    )
    deterministic = BooleanField(
        label='Sign using RFC6979 standard',
        default=False,
    )
    electrum = BooleanField(
        label='Sign using Electrum standard',
        default=False,
    )
    submit = SubmitField(label='Sign message')


class VerifyForm(FlaskForm):
    address = StringField(
        label='Bitcoin Address',
        validators=[DataRequired()],
    )
    message = TextAreaField(
        label='Message',
        validators=[DataRequired()],
    )
    signature = StringField(
        label='Signature',
        validators=[DataRequired()],
    )
    electrum = BooleanField(
        label='Verify using Electrum standard',
        default=False,
    )
    submit = SubmitField(label='Verify message')
