from flask import Blueprint, jsonify, request, make_response, render_template, session
from flask_login import current_user, login_required
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
    return make_response(
        render_template('login.html'),
        201
    )

@users.route('/nickname')
@login_required
def nickname():
    return jsonify({
        'nickname': current_user.nickname
    })

@users.route('/edit', methods=['POST'])
@login_required
def edit():
    user_service.update_nickname(request.form['nickname'])
    return render_template('home.html', nickname=current_user.nickname)

@auth.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    user = auth_service.login(request.form)
    if user:
        return render_template('home.html')
    return render_template('login.html', message='Wrong credentials!')

@rooms.route('/join', methods=['POST'])
def create_room():
    room = request.form.get('room')
    message = {'user': current_user.nickname, 'message': f"Heeey!! I'm playing on room: <b>{room}<b>"}
    socketio.emit('message', message)
    session['room'] = room
    return render_template('game.html', room=session['room'], nickname=current_user.nickname)
