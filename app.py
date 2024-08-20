# from flask import Flask, render_template, url_for, redirect, jsonify, request
from flask import *
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import update
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from forms import RegisterForm, loginForm, checkoutForm
import time
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
    javascriptOwner = db.Column(db.Boolean, default=True, nullable=False)
    pythonOwner = db.Column(db.Boolean, default=False, nullable=False)
    javaOwner = db.Column(db.Boolean, default=False, nullable= False)
'''
class Courses(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    # user = db.relationship('User', backref='courses')
    javascriptOwner = db.Column(db.Boolean, default=False, nullable=False)
    pythonOwner = db.Column(db.Boolean, default=False, nullable=False)
    javaOwner = db.Column(db.Boolean, default=False, nullable= False)
'''


with app.app_context():
    db.create_all()
    



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
        "ownsPython": user.pythonOwner,
        "ownsJava": user.javaOwner,
        "ownsJavascript": user.javascriptOwner
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
        try:
            user = User.query.filter_by(username=form.username.data).first() # Checking to see if user is in database
            if user:
                if bcrypt.check_password_hash(user.password, form.password.data): # Comparing user password and form password
                    login_user(user)
                    return redirect(url_for('userdash'))
                else:
                    flash("Please Enter Valid Credentials", 'error')
        except:
            flash("An error occurreed, try again later", 'error')
    return render_template('login.html', form=form)   

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    try:
        if(form.validate_on_submit()):
            if(User.query.filter_by(username = RegisterForm.username.data)):
                print("error")
            else:
                hashed_password = bcrypt.generate_password_hash(form.password.data)
                new_user = User(username=form.username.data, password=hashed_password)
                db.session.add(new_user)
                db.session.commit()
                return redirect(url_for('login'))
    except:
        # NOTE
        # use flash instead
        flash("Username Already In Use", 'error')
        print("an error has occured")
    
    return render_template('register.html', form=form)

def checkDate(value):
    temp = value.split('/')
    if((len(temp[0]) != 0 or len(temp[1]) <= 3) and (temp[1].isdigit() and temp[2].isdigit)):
        return True
    else:
        return False

@app.route('/checkout', methods=['GET', 'POST'])
@login_required
def checkout():
    purchasing = request.args.get('purchasing')
    form = checkoutForm()
    user = User.query.filter_by(id = str(current_user.id)).first()
    passes = True
    print(1)
    if(form.validate_on_submit()):
        print('Test1')
        if((len(form.cc_number.data.replace(" ", "")) == 16) and (form.first_name.data.isalpha()) and (form.last_name.data.isalpha()) and (form.security_code.data.isdigit() and len(form.security_code.data) == 3) or checkDate(form.expiration_date.data)):
            print('Test2')
            if(form.purchasing.data == 'python'):
                print('Test3')
                user.pythonOwner = True
                db.session.commit()
                flash('Python Added')
                return render_template('userdash.html', user_id = str(user.id))
            elif(form.purchasing.data == 'javascript'):
                print('Test4')
                user.javascriptOwner = True
                db.session.commit()
                flash('Javascript Added')
                return render_template('userdash.html', user_id = str(user.id))
            elif(form.purchasing.data == 'java'):
                print('Test5')
                user.javaOwner = True
                db.session.commit() 
                flash('Java Added')
                return render_template('userdash.html', user_id = str(user.id))
            else:
                flash('Error Occured, Please try again')
    # print('hello')
    # time.sleep(10)
    return render_template('checkout.html', user_id = str(user.id), username = str(user.username), form=form, purchasing = purchasing)
        
    
'''
@app.route('/checkout', methods=['GET', 'POST'])
@login_required
def checkout():
    user = User.query.filter_by(id = str(current_user.id)).first()
    return render_template('checkout.html', user_id = str(user.id), username = str(user.username))
'''


@app.route('/userdash/pythoncourse', methods=['GET', 'POST'])
@login_required
def pythoncourse():
    user = User.query.filter_by(id = str(current_user.id)).first()
    return render_template('pythoncourse.html', user_id = str(user.id), username = str(user.username), price=50)


@app.route('/userdash/javascriptcourse', methods=['GET'])
@login_required
def javascriptcourse():
    user = User.query.filter_by(id = str(current_user.id)).first()
    return render_template('javascriptcourse.html', user_id = str(user.id), username = str(user.username), price=40)

@app.route('/userdash/javacourse', methods=['GET', 'POST'])
@login_required
def javacourse():
    user = User.query.filter_by(id = str(current_user.id)).first()
    return render_template('javacourse.html', user_id = str(user.id), username = str(user.username), price=30)

@app.route('/userdash', methods=['GET', 'POST'])
@login_required
def userdash():
    
    user = User.query.filter_by(id = str(current_user.id)).first()
    return render_template('userdash.html', user_id = str(user.id), ownsPython = user.pythonOwner, ownsJava = user.javaOwner, ownsJavascript = user.javascriptOwner)







if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000,debug=True)


# 24:40
# https://www.youtube.com/watch?v=71EU8gnZqZQ&t=909s


# https://www.geeksforgeeks.org/login-and-registration-project-using-flask-and-mysql/
# https://www.youtube.com/watch?v=2mbHyB2VLYY