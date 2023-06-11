from flask import Blueprint, redirect, request, jsonify, make_response, render_template, flash
from flask_login import current_user
from serializers import user_serializer
from services import auth_service, user_service


users = Blueprint('users', __name__)
auth = Blueprint('auth', __name__)


@users.route('/register', methods=['POST', 'GET'])
def create():
    if request.method == 'GET':
        return render_template('register.html')
    data = request.form
    user_service.create_user(data)
    return make_response(
        render_template('login.html'),
        201
    )


@auth.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    user = auth_service.login(request.form)
    if user:
        return render_template('home.html')
    return render_template('login.html', message='Wrong credentials!')
