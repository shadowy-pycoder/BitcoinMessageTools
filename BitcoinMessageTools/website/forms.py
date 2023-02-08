from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, PasswordField, BooleanField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from bitcoin_message_tool import bmt


class SignForm(FlaskForm):

    def validate_private_key(self, field: FlaskForm):
        try:
            private_key = bmt.to_int(field.data)[0]
        except bmt.PrivateKeyError as err:
            raise ValidationError(err.args)
        self.private_key = private_key

    private_key = StringField(
        label='Private Key',
        validators=[DataRequired()],
    )
    address_type = SelectField(
        label='Address Type',
        validators=[DataRequired()],
        choices=[('p2pkh', 'P2PKH'), ('p2wpkh-p2sh', 'P2WPKH-P2SH'), ('p2wpkh', 'P2WPKH')]
    )
    message = StringField(
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


class VerifyForm(FlaskForm):
    ...
