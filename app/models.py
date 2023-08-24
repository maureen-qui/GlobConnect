from app import db
from flask_login import UserMixin

# User Model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    collaboration_groups = db.relationship('CollaborationGroup', backref='creator', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

# Collaboration Group Model
class CollaborationGroup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    creator_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"CollaborationGroup('{self.name}', '{self.creator_id}')"
