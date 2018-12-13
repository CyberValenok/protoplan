from flask import render_template
from dl import app
from dl.forms import RegistrationForm



@app.route("/")
def hello():
    form = RegistrationForm()
    return render_template('login.html', form=form)


@app.route("/index")
def index_1():
    user = {'username':'Pytoha'}
    return render_template('main.html', title='About user', user=user)
