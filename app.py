from flask import Flask, render_template
from flask_socketio import SocketIO, send


app = Flask(__name__)

# Set secret key to enable session storage
app.config['SECRET'] = 'secret!'

# Initialize socketio
socketio = SocketIO(app, cors_allowed_origins='*')

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)
    if message != 'User connected!':
        send(message, broadcast=True)

@app.route('/')
def index():
    return render_template('chat.html')

if __name__ == '__main__':
    socketio.run(app, debug=True, port=5000, allow_unsafe_werkzeug=True)
