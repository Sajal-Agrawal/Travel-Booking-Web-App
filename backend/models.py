# models.py
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    profile_pic = db.Column(db.String(255), default='static/uploads/default-avatar.png')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Booking(db.Model):
    __tablename__ = 'bookings'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    service_type = db.Column(db.String(50), nullable=False)
    pickup_location = db.Column(db.String(255), nullable=False)
    dropoff_location = db.Column(db.String(255), nullable=False)
    pickup_date = db.Column(db.String(50), nullable=False)
    pickup_time = db.Column(db.String(50), nullable=False)
    dropoff_date = db.Column(db.String(50))
    dropoff_time = db.Column(db.String(50))
    passengers = db.Column(db.Integer)
    distance = db.Column(db.Float)
    vehicle_type = db.Column(db.String(50))
    fare = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default='Pending')
    booking_date = db.Column(db.DateTime, default=datetime.utcnow)
    token = db.Column(db.String(16))  # Added token column

    user = db.relationship('User', backref=db.backref('bookings', lazy=True))