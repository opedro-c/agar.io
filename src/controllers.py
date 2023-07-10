from flask import Blueprint, jsonify, request, render_template, redirect, url_for
from flask_login import current_user, login_required, logout_user
from game import socketio
from services import auth_service, user_service


users = Blueprint('users', __name__)
auth = Blueprint('auth', __name__)
rooms = Blueprint('room', __name__, url_prefix='/rooms')


@users.route('/register', methods=['POST', 'GET'])
def create():
    if request.method == 'GET':
        return render_template('register.html')
    data = request.form
    user_service.create_user(data)
    return redirect(url_for('auth.login'))

@users.route('/info')
@login_required
def info():
    return jsonify({
        'nickname': current_user.nickname,
        'color': current_user.color
    })

@users.route('/edit', methods=['POST'])
@login_required
def edit():
    user_service.update(request.form)
    return redirect(url_for('home'))

@users.route('/home')
@login_required
def home():
    return render_template('home.html', nickname=current_user.nickname, color=current_user.color)

@auth.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    user = auth_service.login(request.form)
    if user:
        return redirect(url_for('users.home'))
    return render_template('login.html', message='Wrong credentials!')

@auth.route('/logout', methods=['POST'])
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@rooms.route('/join', methods=['POST'])
def create_room():
    room = request.form.get('room')
    message = {'user': current_user.nickname, 'message': f"Heeey!! I'm playing on room: <b>{room}<b>"}
    socketio.emit('message', message)
    data = { 'room': room, 'nickname': current_user.nickname, 'color': current_user.color }
    return render_template('game.html', **data)
