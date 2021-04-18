from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

login_manager = LoginManager()

db = SQLAlchemy()

def create_app(config):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config)
    db.init_app(app)

    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "auth.login"

    from app import models

    # temporary route
    @app.route('/')
    def hello_world():
        return 'Hello, World!'

    return app
