"""Data models."""
from sqlalchemy import String
from . import db
from sqlalchemy.dialects import postgresql


class User(db.Model):
    """Data model for user accounts."""

    __tablename__ = 'users'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    username = db.Column(
        db.String(50),
        index=False,
        unique=True,
        nullable=False
    )

    def __repr__(self):
        return '<User {}>'.format(self.username)    


class Contact(db.Model):

    __tablename__ = 'contact'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id'),
        index=False,
        unique=True,
        nullable=False
    )
    phone_number = db.Column(
        db.String(15),
        index=False,
        unique=False
    )
    email = db.Column(
        db.String(15),
        index=False,
        unique=False
    )

    websites = db.Column(
        postgresql.ARRAY(String),
        index=False,
        unique=False
    )


    def __repr__(self):
        return '<Contact {}>'.format(self.user_id)
    
class Education(db.Model):

    __tablename__ = 'education'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id'),
        index=False,
        unique=True,
        nullable=False
    )
    school_name = db.Column(
        db.String(50),
        index=False,
        unique=False
    )    
    degree = db.Column(
        db.String(50),
        index=False,
        unique=False
    )
    location = db.Column(
        db.String(50),
        index=False,
        unique=False
    )
    time_range = db.Column(
        db.String(50),
        index=False,
        unique=False
    )

    def __repr__(self):
        return '<Education {}>'.format(self.user_id)
    
class Experience(db.Model):

    __tablename__ = 'experience'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id'),
        index=False,
        unique=True,
        nullable=False
    )
    company = db.Column(
        db.String(30),
        index=False,
        unique=False
    )    
    position = db.Column(
        db.String(50),
        index=False,
        unique=False
    )
    region = db.Column(
        db.String(20),
        index=False,
        unique=False
    )
    date_start = db.Column(
        db.DateTime,
        index=False,
        unique=False
    )
    body = db.Column(
        postgresql.ARRAY(String),
        index=False,
        unique=False
    )

    def __repr__(self):
        return '<Experience {}>'.format(self.user_id)

class Skill(db.Model):

    __tablename__ = 'skills'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id'),
        index=False,
        unique=True,
        nullable=False
    )
    category = db.Column(
        db.String(30),
        index=False,
        unique=False
    )
    body = db.Column(
        postgresql.ARRAY(String),
        index=False,
        unique=False
    )

    def __repr__(self):
        return '<Skill {}>'.format(self.user_id)
    
class Project(db.Model):

    __tablename__ = 'projects'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id'),
        index=False,
        unique=True,
        nullable=False
    )
    title = db.Column(
        db.String(30),
        index=False,
        unique=False
    )
    body = db.Column(
        postgresql.ARRAY(String),
        index=False,
        unique=False
    )

    def __repr__(self):
        return '<Project {}>'.format(self.user_id)
    
