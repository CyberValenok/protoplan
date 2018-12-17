from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import PasswordField
from wtforms import SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo

class Login(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign in')

class RegistrationForm(FlaskForm):
    username= StringField('Username', validators=[DataRequired()])
    email= StringField('E-mail', validators=[DataRequired(), Email()])
    password= PasswordField ('Password', validators=[DataRequired()])
#    password2= PasswordField ('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit= SubmitField ('Sign up')

    #def validate_username(self, username):
    #    username=
