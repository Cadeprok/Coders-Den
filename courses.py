from flask import Flask, render_template, url_for, redirect, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from forms import RegisterForm, loginForm, checkoutForm



from app import User
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