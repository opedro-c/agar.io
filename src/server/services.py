from models import db
from serializers import user_serializer
from werkzeug.security import generate_password_hash


class UserService:

    def create_user(self, data):
        user = user_serializer.load(data)
        user.password = generate_password_hash(user.password, method='sha256')
        db.session.add(user)
        db.session.commit()
        return user_serializer.dump(user)


user_service = UserService()
