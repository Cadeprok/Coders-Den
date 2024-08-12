from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask import Flask, render_template, url_for, redirect, jsonify, request
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_wtf import FlaskForm

class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(
        min=4,max=20)], render_kw={"placeholder":"Username"})
    
    password = PasswordField(validators=[InputRequired(), Length(
        min=4,max=50)], render_kw={"placeholder":"Password"})
    
    submit = SubmitField("Register")

    def validate_username(self, username):
        existing = User.query.filter_by(
            username = username.data).first()
        print("1")
        if existing:
            raise ValidationError(
                "That Username already exists, please choose a different one."
            )
class loginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(
        min=4,max=20)], render_kw={"placeholder":"Username"})
    
    password = PasswordField(validators=[InputRequired(), Length(
        min=4,max=50)], render_kw={"placeholder":"Password"})
    
    submit = SubmitField("Login")

class checkoutForm(FlaskForm):

    cc_number = StringField(validators=[InputRequired(), Length(min=16, max=20)], render_kw={"placeholder":"Credit Card Number"})
    first_name = StringField(validators=[InputRequired(), Length(min=1, max=20)], render_kw={"placeholder":"First Name"})
    last_name = StringField(validators=[InputRequired(), Length(min=1, max=20)], render_kw={"placeholder":"Last Name"})
    expiration_date = StringField(validators=[InputRequired(), Length(min=4, max=5)], render_kw={"placeholder":"Expiration Date"})
    security_code = StringField(validators=[InputRequired(), Length(min=3, max=3)], render_kw={"placeholder":"Security Code"})
    purchasing = SelectField('Programming Language', choices=[('python', 'Python'), ('java','Java'), ('javascript', 'Javascript')], validators=[InputRequired()])

    submit = SubmitField("Purchase")



from app import User