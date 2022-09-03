from flask import Flask, session, request, render_template
from flask_socketio import SocketIO
import random, string
import datab

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bbgfty45y35ehe4343h'
socketio = SocketIO(app)

@app.route('/', methods = ['GET', 'POST'])
def home():
    return render_template('home.html')

def login():
    if request.method == 'POST':
        serverCode = request.form.get('servercode')
        session['username'] = request.form['username']
        create_connection()
        if searchname(conn, servercode) == True:
            return redirect(url_for('chat'))
        else:
            return redirect(url_for('home'))
        
def createServer():
    if request.method == 'POST':
        session['username'] = request.form['usertwo']
        topic = request.form.get('stopic')
        characters = string.ascii_letters + string.digits
        code = ''.join(random.choice(characters) for i in range(6))
        create_connection()
        if addData(code, topic):
            return redirect(url_for('chat'))
        else:
            return redirect(url_for('home'))

@app.route('/chat/<servercode>/')
def chat():
    if searchname(conn, servercode) and 'username' in session:
        return render_template('chat1.html', servercode=servercode, username=session["username"])
    return redirect(url_for('home'))
    

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)

if __name__ == '__main__':
    socketio.run(app, debug=True)