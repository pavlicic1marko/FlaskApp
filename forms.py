from flask_wtf import FlaskForm
from  wtforms import SelectField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = SelectField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = SelectField('Email', validators=[DataRequired(), Email])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=2, max=20)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo(password)])


class LoginForm(FlaskForm):
    email = SelectField('Email', validators=[DataRequired(), Email])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=2, max=20)])
    remember = BooleanField('Remember Me?')
    submit = SubmitField('Login')
