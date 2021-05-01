# main.py
from datetime import datetime
from . import db
from .models import User
from .models import Workout
from flask import Blueprint, render_template, redirect, url_for, request, flash, abort
from flask_login import current_user, login_required
from flask import Flask, session, render_template
from sqlalchemy import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)
    # logs user into main profile page


@main.route('/workout/all')
@login_required
def user_workouts():
    user = User.query.filter_by(email=current_user.email).first_or_404()
    workouts = user.workouts
    return render_template('logged_workouts.html', workouts=workouts, user=user)
    # show users the page with all of their workouts


@main.route('/workout')
@login_required
def new_workout():
    return render_template('add_workout.html')
    # grants access to page that allows for logging a new workout
    

@main.route('/workout', methods=['POST'])
@login_required
def add_workout_post():
    print('here1')
    miles = request.form['miles']
    comment = request.form['comment']
    print('here2')
    workout = Workout(miles=miles, comment=comment, date_posted=datetime.now(), user_id=current_user.id)
    db.session.add(workout)
    db.session.commit()
    return render_template('logged_workouts.html', workouts=current_user.workouts, user=current_user)


@main.route('/workout/<int:workout_id>/update')
@login_required
def update_workout(workout_id):
    workout = Workout.query.get_or_404(workout_id)
    return render_template('update_workout.html', workout=workout)

@main.route('/workout/<int:workout_id>/update', methods=['POST'])
@login_required
def post_update_workout(workout_id):
    print('here')
    workout = Workout.query.get_or_404(workout_id)
    workout.miles = request.form['miles']
    workout.comment = request.form['comment']
    db.session.commit()
    flash('Your log has been updated!')
    return render_template('update_workout.html', workout=workout)
    # allows user to update a past log if the distance/comment was incorrect


@main.route('/workout/<int:workout_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_workout(workout_id):
    workout = Workout.query.get_or_404(workout_id)
    db.session.delete(workout)
    db.session.commit()
    flash('Your log has been deleted!')
    return redirect(url_for('main.user_workouts'))
    #allows user to delete a logged workout entry
