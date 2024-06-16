from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'SECRET_KEY'

    from .views import view
    app.register_blueprint(view, url_prefix = '/')

    return app