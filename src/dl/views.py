from flask import render_template
from flask import flash
from flask import redirect
from dl import app
from dl.forms import RegistrationForm



@app.route("/", methods=['GET','POST'])
def hello():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Data entered is normal, but registration has not yet been added.Sry!')
    return render_template('registration.html', form=form)


@app.route("/index")
def index_1():
    user = {'username':'Pytoha'}
    return render_template('main.html', title='About user', user=user)

@app.route("/signin")
def login():
    return render_template('login.html')
