from flask import Flask
from flask import request
from flask import render_template
import flask

app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return "show_the_login_form()"



@app.route('/')
def hello(name=None):
    return render_template('index.html', name=name)
