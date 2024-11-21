from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(data):
    print(f"Message: {data}")
    emit('message', data, broadcast=True)  # Broadcast to all clients

if __name__ == '__main__':
    socketio.run(app, debug=True)
