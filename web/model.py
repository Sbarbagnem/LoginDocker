from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask_script import Manager
import sqlalchemy
from web import db

class User(db.Model):

    
    email = db.Column(db.String(45), primary_key=True)
    password = db.Column(db.String(45), unique=False)
    name = db.Column(db.String(45), unique=False)
    surname = db.Column(db.String(45), unique=False)
    visit = db.Column(db.Integer, unique=False)
    
    def __init__(self, name, email, password, surname, visit):
        
        self.name = name
        self.email = email
        self.password = password
        self.surname = surname
        self.visit = visit

    def __repr__(self):
        return '<User %r>' % self.name
