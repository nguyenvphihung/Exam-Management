from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()
class Question(db.Model):
 id = db.Column(db.Integer, primary_key=True)
 question_text = db.Column(db.Text, nullable=False)
 choices = db.Column(db.Text, nullable=False)
 correct_answer = db.Column(db.String(100), nullable=False)
 difficulty_level = db.Column(db.Integer, nullable=False)
 category = db.Column(db.String(100), nullable=False)
 
class User(db.Model, UserMixin):
 id = db.Column(db.Integer, primary_key=True)
 username = db.Column(db.String(50), unique=True, nullable=False)
 email = db.Column(db.String(100), unique=True, nullable=False)
 password = db.Column(db.String(100), nullable=False)
 role = db.Column(db.String(10), nullable=False)