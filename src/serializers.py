from flask_marshmallow import Marshmallow
from models import User


ma = Marshmallow()

class UserSerializer(ma.SQLAlchemyAutoSchema):
    
    class Meta:
        model = User
        load_instance = True


user_serializer = UserSerializer()
