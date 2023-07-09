from flask import request
from flask_socketio import SocketIO, emit, join_room

socketio = SocketIO()

@socketio.on('message')
def message(data):
    emit('message', data, broadcast=True)


@socketio.on('position')
def position(data):
    emit('position', data, to=data['room'])

@socketio.on('join')
def join(data):
    join_room(data['room'], request.sid)
