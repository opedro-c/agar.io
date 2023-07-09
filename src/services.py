from flask_login import login_user, current_user
from models import db, User
from serializers import user_serializer
from werkzeug.security import generate_password_hash, check_password_hash


class UserService:

    def create_user(self, data):
        user = user_serializer.load(data)
        user.password = generate_password_hash(user.password, method='sha256')
        db.session.add(user)
        db.session.commit()
        return user
    
    def update(self, data):
        user = User.query.filter(User.id == current_user.id).first()
        user.nickname = data['nickname']
        user.color = data['color']
        db.session.commit()
        return user

    
    def get_user_by_email(self, data):
        user = User.query.filter_by(email=data).first()
        return user


user_service = UserService()


class AuthService:

    def login(self, data):
        user = user_service.get_user_by_email(data.get('email'))
        if not user:
            return None
        password_ok = check_password_hash(user.password, data.get('password'))
        if not password_ok:
            return None
        login_ok = login_user(user)
        if not login_ok:
            return None
        return user


auth_service = AuthService()
