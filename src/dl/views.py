from flask import render_template
from app import app



@app.route("/")
def hello():
    return render_template('login.html')


@app.route("/index")
def index_1():
    user = {'username':'Pytoha'}
    return render_template('main.html', title='About user', user=user)
