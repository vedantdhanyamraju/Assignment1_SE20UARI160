from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(_name_)
socketio = SocketIO(app)

@app.route('/')
def index():
    return "Server is running"

@socketio.on('send_message')
def handle_message(data):
    message = data['message']
    print("Received message:", message)
    emit('response', {'response': 'Message received successfully!'})

if _name_ == '_main_':
    socketio.run(app, debug=True,port=8888)