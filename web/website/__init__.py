from flask import Flask
import os


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
    app.config['DEBUG'] = os.environ.get('DEBUG')
    from .views import views, page_not_found
    app.register_blueprint(views, url_prefix='/')
    app.register_error_handler(404, page_not_found)
    return app
