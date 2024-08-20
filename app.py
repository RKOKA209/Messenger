from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@socketio.on('message')
def handle_message(data):
    print('received message: ' + data)
    if data != "User Connected":
        send(data, broadcast=True)

@socketio.on('image-upload')
def imageUpload(image):
    emit('send-image', image, broadcast = True)


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    socketio.run(app)
    
