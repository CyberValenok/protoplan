from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import PasswordField
from wtforms import SubmitField
from wtforms.validators import DataRequired

class RegistrationForm(FlaskForm):
    username= StringField('Username', validators=[DataRequired()])
    email= StringField('E-mail', validators=[DataRequired()])
    password= PasswordField ('Password', validators=[DataRequired()])
    submit= SubmitField ('Sign up')
