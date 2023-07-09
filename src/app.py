from flask import Flask, render_template
from flask_cors import CORS
from flask_login import LoginManager
from flask_migrate import Migrate
from game import socketio
from game import socketio
from models import db, User
from secrets import token_hex
from serializers import ma


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///agario.db'
    app.config['SECRET_KEY'] = token_hex(16)

    login_manager = LoginManager()
    login_manager.init_app(app)

    socketio.init_app(app, cors_allowed_origins='*')

    db.init_app(app)
    ma.init_app(app)

    from controllers import users, auth, rooms
    app.register_blueprint(users)
    app.register_blueprint(auth)
    app.register_blueprint(rooms)

    @app.route('/')
    def home():
        return render_template('register.html')

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    Migrate(app, db)

    return app