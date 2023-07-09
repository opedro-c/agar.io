from flask import session
from flask_socketio import SocketIO, emit

socketio = SocketIO()

@socketio.on('message')
def message(data):
    emit('message', data, broadcast=True)


@socketio.on('position')
def position(data):
    emit('position', data, to=data['room'])
