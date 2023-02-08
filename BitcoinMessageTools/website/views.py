from flask import Blueprint, render_template


views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@views.route('/sign', methods=['GET', 'POST'])
def sign_page():
    return render_template('sign.html')


@views.route('/verify', methods=['GET', 'POST'])
def verify_page():

    return render_template('verify.html')
