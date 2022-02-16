from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo #error so we had to pip install email_validator

#DEBUG-->syntax error-->bug
#   ^
#   |
# logical error-->bug(you aren't running the right logic)

class RegistrationForm(FlaskForm):
    username=StringField('Username',
                         validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('password',
                             validators=[DataRequired()])
    email=StringField('Email',
                      validators=[DataRequired(), Email()])
    confirmpassword=PasswordField('ConfirmPassword',
                                  validators=[DataRequired(), EqualTo('password')])
    submit=SubmitField('Sign up today', validators=[DataRequired()])