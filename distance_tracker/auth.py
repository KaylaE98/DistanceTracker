# auth.py file

from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from .models import User
from . import db

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('login.html')
    #loads login page


@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    # determines if a user already exists with that name
    # compares the entered password after being hashed with the hashed password already saved

    if not user or not check_password_hash(user.password, password):
        flash('Please check to see if your email and password are correct and then try again.')
        return redirect(url_for('auth.login'))
        # if the password is incorrect or the user does not yet exist, the page reloads
    
    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))
    # if the authentication works, then the user is redirected to their profile page

@auth.route('/signup')
def signup():
    return render_template('signup.html')
    # allows new user to sign up

@auth.route('/signup', methods=['POST'])
def signup_post():

    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()

    print(user)
    # the email address already exists in the database if a user is returned

    if user:  
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))
        # if found, redirects the user back to signup page to try signing up again

    
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))
    # Creates the new user with the entered information
    # Hashes the password without saving plaintext version for added security

    db.session.add(new_user)
    # adds the new user to the database
    db.session.commit()

    return redirect(url_for('auth.login'))
    # redirects user to the login page

@auth.route('/new', methods=['POST'])
def new_post():
    id = request.form.get('id')
    email = request.form.get('email')
    password = request.form.get('password')
    name = request.form.get('name')
    workout = request.form.get('workout')
    
    flash('Your workout was saved!')
    return redirect(url_for('main.user_workouts'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
    # logs user out
