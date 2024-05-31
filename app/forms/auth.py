from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo, Regexp, ValidationError

class RegistrationForm(FlaskForm):
  Username = StringField('Full_name',validators=[DataRequired()])
  email = StringField('Email',validators=[DataRequired(),Email()])
  phone = StringField('phone',validators=[DataRequired(),Length(min=10,max=10,message="Phone number must be 10 digits")])
  password = PasswordField('Password',validators=[DataRequired(),Regexp(regex=r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$',message="Password must be at least 8 characters long and contain both letters and numbers.")])
  confirm_password = PasswordField('Confirm_password',validators=[DataRequired(),EqualTo('Password',message="Password must match.")])
  submit = SubmitField('Register')

  