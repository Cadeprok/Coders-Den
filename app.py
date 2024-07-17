from flask import Flask, render_template, url_for, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt
from flask_cors import CORS


app = Flask(__name__)
# Creates database instance

# Connects to database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'thisisasecretkey'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
CORS(app)


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)
class Courses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db. ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref='courses')
    javascriptOwner = db.Column(db.Boolean, default=False, nullable=False)
    pythonOwner = db.Column(db.Boolean, default=False, nullable=False)
    javaOwner = db.Column(db.Boolean, default=False, nullable= False)

class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(
        min=4,max=20)], render_kw={"placeholder":"Username"})
    
    password = PasswordField(validators=[InputRequired(), Length(
        min=4,max=50)], render_kw={"placeholder":"Password"})
    
    submit = SubmitField("Register")

    def validate_username(self, username):
        existing = User.query.filter_by(
            username = username.data).first()
        
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


with app.app_context():
    db.create_all()
    print('DB Created')



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = loginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first() # Checking to see if user is in database
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data): # Comparing user password and form password
                login_user(user)
                return redirect(url_for('userdash'))
    return render_template('login.html', form=form)   

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('register.html', form=form)   

@app.route('/userdash', methods=['GET', 'POST'])
@login_required
def userdash():
    return render_template('userdash.html')



@app.route('/get_data')
def get_data():
    form = loginForm()
    #dict
    #dict.update({"ownsPython": User.query.filter_by(username = form.username.data).first().javascriptOwner})
    #dict.update({"ownsJava" : User.query.filter_by(username = form.username.data).first().pythonOwner})
    #dict.update({"ownsPython" : User.query.filter_by(username = form.username.data).first().ownsJavascript})
    #dict = jsonify(dict)
    data = {
        "ownsPython": str(User.query.filter_by(username = form.username.data).first().javascriptOwner),
        "ownsJava" : str(User.query.filter_by(username = form.username.data).first().pythonOwner),
        "ownsPython" : str(User.query.filter_by(username = form.username.data).first().ownsJavascript)
    }
    return jsonify(data)




if __name__ == '__main__':
    app.run(debug=True)


# 24:40
# https://www.youtube.com/watch?v=71EU8gnZqZQ&t=909s


# https://www.geeksforgeeks.org/login-and-registration-project-using-flask-and-mysql/
# https://www.youtube.com/watch?v=2mbHyB2VLYY