from flask import Blueprint, request, jsonify
from services import user_service


users = Blueprint('users', __name__, url_prefix='/users')


@users.route('/create', methods=['POST'])
def create():
    print(request.form)
    data = request.form
    user = user_service.create_user(data)
    return jsonify(user), 201
