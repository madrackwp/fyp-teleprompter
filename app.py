from flask import Flask
from flask import render_template
from markupsafe import escape
from service import *

from flask_socketio import SocketIO
from flask_socketio import emit

import time

app = Flask(__name__)
socketio = SocketIO(app, async_mode = "eventlet")

x = 0


@app.route("/")
def hello_world():
    return render_template("home.html")


@socketio.on("update_variable")
def update_variable():
    x += 1
    time.sleep(5)
    emit("variable_update", x, broadcast=True)

if __name__ == "__main__":
    app.run(debug=True, port=8000)
    socketio.run(app)
