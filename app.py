from flask import Flask, render_template, url_for, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt
import string
import random


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    username = db.Column(db.String(16), nullable=False, unique=True)
    password = db.Column(db.String(32), nullable=False)



class registerForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=6, max=16)], render_kw={"placeholder": "password"})
    password = StringField(validators=[InputRequired(), Length(min=8, max=32)], render_kw={'placeholder': 'Password'})
    submit = SubmitField('Submit')


class loginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=6, max=16)], render_kw={"placeholder": "password"})
    password = StringField(validators=[InputRequired(), Length(min=8, max=32)], render_kw={'placeholder': 'Password'})
    submit = SubmitField('Submit')

def generateRandom():
    login = loginForm
    val = User.query.filter_by(login.username).id
    return string(val) + ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=4))



@app.route('/login.html', methods=['GET', 'POST'])
def login():
    form = loginForm


    if form.validate_on_submit():
        validator = User.query.filter_by(username = form.username.data.first)
        if validator:
            if Bcrypt.check_password_hash(validator.password, validator.password.data):
                login_user(validator)
                


@app.route('/register.html', methods=['GET', 'POST'])
def register():
    form = registerForm

    if form.validate_on_submit():
        hp = Bcrypt.generate_password_hash(form.password.data)
        user = User(username = form.username.data.first, password = hp)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    

@app.route('/userdash.html', methods=['GET', 'POST'])
def userdash():
    return redirect(url_for('userdash'))


@app.route('/' + generateRandom() +  '/python.html', methods=['GET', 'POST'])
def python():
    return redirect(url_for(''))



if __name__ == '__main__':
    app.run(debug=True)


# https://www.digitalocean.com/community/tutorials/how-to-use-flask-sqlalchemy-to-interact-with-databases-in-a-flask-application