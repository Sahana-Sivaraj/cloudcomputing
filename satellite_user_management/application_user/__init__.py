# applicationn/__init__.py
import os
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import config as config

db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    environment_configuration = config.ProductionConfig
    app.config.from_object(environment_configuration)
    app.app_context().push()
    db.init_app(app)
    login_manager.init_app(app)
    with app.app_context():
        from application_user.models import User
        db.create_all()
        from application_user.user_api import user_api_blueprint
        app.register_blueprint(user_api_blueprint)
        return app
