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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///UserDatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'thisisasecretkey'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    username = db.Column(db.String(16), nullable=False, unique=True)
    password = db.Column(db.String(32), nullable=False)
    ownsPython = db.Column(db.Boolean, default=False, nullable=False)
    ownsJava = db.Column(db.Boolean, default=False, nullable=False)
    ownsJavascript = db.Column(db.Boolean, default=False, nullable=False)




class loginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=6, max=16)], render_kw={"placeholder": "Username"})
    password = StringField(validators=[InputRequired(), Length(min=8, max=32)], render_kw={'placeholder': 'Password'})
    submit = SubmitField('Login')


class registerForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=6, max=16)], render_kw={"placeholder": "Username"})
    password = StringField(validators=[InputRequired(), Length(min=8, max=32)], render_kw={'placeholder': 'Password'})
    submit = SubmitField('Register')


def generateRandom():
    login = loginForm
    val = User.query.filter_by(username = login.username).first
    val = val.id
    return string(val) + ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=4))



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login.html', methods=['GET', 'POST'])
def login():
    form = loginForm()


    if form.validate_on_submit():
        validator = User.query.filter_by(username = form.username.data).first()
        if validator:
            if bcrypt.check_password_hash(validator.password, form.password.data):
                login_user(validator)
                # return redirect(url_for('userdash'))
                return render_template('userdash.html', form=form)
    else:
        return render_template('login.html', form=form)
                


@app.route('/register.html', methods=['GET', 'POST'])
def register():
    form = registerForm()

    if form.validate_on_submit():
        hp = bcrypt.generate_password_hash(form.password.data)
        user = User(username = form.username.data, password = hp)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    else:
        return render_template('register.html', form=form)
    

@app.route('/userdash.html', methods=['GET', 'POST'])
def userdash():
    return redirect(url_for('userdash'))


@app.route('/get_data')
def get_data():
    form = loginForm()
    dict
    dict.update({"ownsPython": User.query.filter_by(username = form.username.data).first().ownsPython})
    dict.update({"ownsJava" : User.query.filter_by(username = form.username.data).first().ownsJava})
    dict.update({"ownsPython" : User.query.filter_by(username = form.username.data).first().ownsJavascript})

    return dict
    

@app.route('/' + 'generateRandom()' +  '/python.html', methods=['GET', 'POST'])
def python():
    return redirect(url_for(''))

if __name__ == '__main__':
    app.run(debug=True)

# https://www.digitalocean.com/community/tutorials/how-to-use-flask-sqlalchemy-to-interact-with-databases-in-a-flask-application