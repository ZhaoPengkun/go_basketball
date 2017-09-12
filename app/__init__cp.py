# -*- coding: UTF-8 –*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from main import main as main_blueprint
from auth import auth as auth_blueprint
from flask_login import LoginManager

db = SQLAlchemy()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    app.register_blueprint(main_blueprint, url_prefix='/main')
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    login_manager.init_app(app)
    db.init_app(app)
    # print "create app success"
    return app
