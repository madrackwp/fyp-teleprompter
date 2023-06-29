from flask import Flask
from flask import render_template
from markupsafe import escape
from service import *

app = Flask(__name__)

@app.route("/")
def hello_world():
    testFunction()
    return render_template('home.html', name="Alex")

# @app.route("/hello")
# def hello():
#     return "<p>Hello!</p>"