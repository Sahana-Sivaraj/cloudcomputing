# application/frontend/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, HiddenField, IntegerField

from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    first_name = StringField('First name', validators=[DataRequired()])
    last_name = StringField('Last name', validators=[DataRequired()])
    email = StringField('Email address', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')


class SatForm(FlaskForm):
    name = StringField('name')
    location = StringField('location')
    healthy = IntegerField('healthy')
    submit = SubmitField('Add')

