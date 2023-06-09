from controllers import users
from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager
from flask_migrate import Migrate
from models import db
from serializers import ma


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///agario.db'

    login_manager = LoginManager()
    login_manager.init_app(app)

    db.init_app(app)
    ma.init_app(app)

    app.register_blueprint(users)

    Migrate(app, db)

    return app