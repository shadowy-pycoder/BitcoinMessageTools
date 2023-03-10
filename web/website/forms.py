from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, BooleanField, TextAreaField
from wtforms.validators import DataRequired


class SignForm(FlaskForm):

    private_key = StringField(
        label='Private Key',
        validators=[DataRequired()],
    )
    address_type = SelectField(
        label='Address Type',
        validators=[DataRequired()],
        choices=[('p2pkh', 'Legacy'), ('p2wpkh-p2sh', 'Nested SegWit'), ('p2wpkh', 'SegWit')]
    )
    message = TextAreaField(
        label='Message',
        validators=[DataRequired()],
    )
    signature = TextAreaField(
        label='Signature', default=None
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
    signature = TextAreaField(
        label='Signature',
        validators=[DataRequired()],
    )
    electrum = BooleanField(
        label='Verify using Electrum standard',
        default=False,
    )
    submit = SubmitField(label='Verify message')
