from flask import Blueprint, request, jsonify
from flask_login import current_user
from serializers import user_serializer
from services import auth_service, user_service


users = Blueprint('users', __name__, url_prefix='/users')
auth = Blueprint('auth', __name__, url_prefix='/auth')


@users.route('/create', methods=['POST'])
def create():
    print(request.form)
    data = request.form
    user = user_service.create_user(data)
    return jsonify(user_serializer.dump(user)), 201


@auth.route('/login', methods=['POST'])
def login():
    user = auth_service.login(request.form)
    if user:
        return user_serializer.dump(user)
    else:
        return {'message': 'wrong credentials'}, 400
   
