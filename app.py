from flask import Flask, render_template, url_for, redirect, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
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
    return User.query.filter_by(id = str(user_id)).first()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)
    # courses = db.relationship('Courses', backref='user', lazy='dynamic')
    javascriptOwner = db.Column(db.Boolean, default=False, nullable=False)
    pythonOwner = db.Column(db.Boolean, default=False, nullable=False)
    javaOwner = db.Column(db.Boolean, default=False, nullable= False)
'''class Courses(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    # user = db.relationship('User', backref='courses')
    javascriptOwner = db.Column(db.Boolean, default=False, nullable=False)
    pythonOwner = db.Column(db.Boolean, default=False, nullable=False)
    javaOwner = db.Column(db.Boolean, default=False, nullable= False)'''

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


with app.app_context():
    db.create_all()
    print('DB Created')



@app.route('/get_data/<user_id>', methods=['GET'])
def get_data(user_id):
    user = load_user(user_id)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    
    '''# Query the Courses model to get the ownership information
    courses = Courses.query.filter_by(owner_id=user.id).first()
    if courses is None:
        return jsonify({"error": "Courses not found for user"}), 404'''
    
    user_data = {
        "ownsPython": str(user.pythonOwner),
        "ownsJava": str(user.javaOwner),
        "ownsJavascript": str(user.javascriptOwner)
    }
    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra
    return jsonify(user_data)
    
    # CURRENT_USER
    # CURRENT_USER
    # CURRENT_USER


    '''print("1")
    form = loginForm()  
    username = form.username.data
    
    user = User.query.filter_by(username=username).first()
    if user is None:
        raise ValueError("User not found")
    
    data = {
        "ownsPython": str(user.pythonOwner),
        "ownsJava": str(user.javaOwner),  # Fixed key
        "ownsJavascript": str(user.ownsJavascript)
    }
    
    return jsonify(data)'''

    '''print("1")
    user = User.query.get(current_user.id)
    courses = Courses.query.filter_by(owner_id = user.id).first()
    data = {
        "ownsPython": str(courses.pythonOwner),
        "ownsJava": str(courses.javaOwner), 
        "ownsJavascript": str(courses.ownsJavascript)
    }
    return jsonify(data)'''


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


@app.route('/userdash/pythoncourse', methods=['GET'])
@login_required
def pythoncourse():
    user = User.query.filter_by(id = str(current_user.id)).first()
    return render_template('pythoncourse.html', user_id = str(user.id), username = str(user.username))


@app.route('/userdash/javascriptcourse', methods=['GET'])
@login_required
def javascriptcourse():
    user = User.query.filter_by(id = str(current_user.id)).first()
    return render_template('javascriptcourse.html', user_id = str(user.id), username = str(user.username))

@app.route('/userdash/javacourse', methods=['GET'])
@login_required
def javacourse():
    user = User.query.filter_by(id = str(current_user.id)).first()
    return render_template('javacourse.html', user_id = str(user.id), username = str(user.username))

@app.route('/userdash', methods=['GET', 'POST'])
@login_required
def userdash():
    
    user = User.query.filter_by(id = str(current_user.id)).first()
    return render_template('userdash.html', user_id = str(user.id))







if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000,debug=True)


# 24:40
# https://www.youtube.com/watch?v=71EU8gnZqZQ&t=909s


# https://www.geeksforgeeks.org/login-and-registration-project-using-flask-and-mysql/
# https://www.youtube.com/watch?v=2mbHyB2VLYY