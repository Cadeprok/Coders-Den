from flask import Flask, render_template, url_for, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User():
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    username = db.Column(db.String(16), nullable=False, unique=True)
    password = db.Column(db.String(32), nullable=False)






class registerForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=6, max=16)], render_kw={"placeholder": "password"})
    password = StringField(validators=[InputRequired(), Length(min=8, max=32)], render_kw={'placeholder': 'Password'})
    submit = SubmitField('Submit')


class loginForm(FlaskForm):
    username = StringField('Username').validators(InputRequired(), min=6, max=16)
    password = StringField('Password').validators(InputRequired(), min=8, max=32)
    submit = SubmitField('Submit')

@route('/login.html', methods=['GET', 'POST'])
def login():
    form = loginForm


    if form.validate_on_submit():
        validator = User.query.filter_by(username = form.username.data.first)
        if validator:
            if Bcrypt.check_password_hash(validator.password, validator.password.data):
                login_user(validator)
                


@route('/register.html')
def register():
    