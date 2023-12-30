from flask_wtf import FlaskForm
from wtforms import PasswordField, BooleanField, SubmitField, StringField
from wtforms.validators import DataRequired, Length, Email


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(6, 20)])
    submit = SubmitField('register')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me?')
    submit = SubmitField('Login')


class News(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    text = StringField('text', validators=[DataRequired()])
    submit = SubmitField('Publish')
