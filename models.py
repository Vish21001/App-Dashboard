from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class App(db.Model):
    __tablename__ = 'apps'
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    subcategory = db.Column(db.String(50))
    developer_name = db.Column(db.String(150))
    downloads = db.Column(db.BigInteger, default=0)
    rating = db.Column(db.Float, default=0.0)
    price = db.Column(db.Float, default=0.0)
    release_date = db.Column(db.Date)
    last_updated = db.Column(db.Date)
    is_active = db.Column(db.Boolean, default=True)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.BigInteger, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.BigInteger, primary_key=True)
    user_id = db.Column(db.BigInteger, db.ForeignKey('users.id'))
    app_id = db.Column(db.BigInteger, db.ForeignKey('apps.id'))
    rating = db.Column(db.Float)
    comment = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
