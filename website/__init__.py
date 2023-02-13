from flask import Flask


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py', silent=True)
    from .views import views, page_not_found
    app.register_blueprint(views, url_prefix='/')
    app.register_error_handler(404, page_not_found)
    return app
