import os
from flask import Flask, render_template
from flask.ext.socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def webprint():
    return render_template('editor-page1.html')

@app.route('/editor-page2')
def webprint2():
    return render_template('editor-page2.html')

@socketio.on('my event', namespace='/test')
def handle_my_custom_event(json):
    print('received json: ' + str(json))
    emit('my response', {'data': 'yo!'})
if __name__ == '__main__':
    socketio.run(app, host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)), debug=True)
