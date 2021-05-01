from flask_login import UserMixin
from datetime import datetime
from . import db
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
     # primary key required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    workouts = db.relationship('Workout', backref='author', lazy=True)
    #saves user to database (username and password)
    #authenticates users
    #provides session management

class Workout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    miles = db.Column(db.Numeric, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    comment = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    #loads all saved workouts to the database


class workout(db.Model):
    def save(workout):
        if workout not in db.session:
            db.session.add(workout)
            db.session.commit()

    def update(workout, data: dict):
        for field, value in data.items():
            setattr(workout, field, value)
        self.save()

    def delete(workout):
        db.session.delete(workout)
        db.session.commit()