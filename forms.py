from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from wtforms.fields.html5 import DateField


class RegistrationForm(FlaskForm):
    firstname = StringField('firstname', validators=[DataRequired(), Length(min=2, max=20)])
    lastname = StringField('lastname', validators=[DataRequired(), Length(min=2, max=20)])
    dob = DateField('Date_of_Birth', format='%Y-%m-%d')
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class Authenticate_Employee_Form(FlaskForm):
    email_ver = StringField('Email', validators=[DataRequired(), Email()])
    password_ver = PasswordField('Password', validators=[DataRequired()])
    submit_ver = SubmitField('login')
