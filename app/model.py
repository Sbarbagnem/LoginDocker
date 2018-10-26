from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import sqlalchemy


app = Flask(__name__)
DATABASE = 'AppDB'
PASSWORD = 'root'
USER = 'root'
HOSTNAME = 'db'

engine = sqlalchemy.create_engine('mysql://%s:%s@%s'%(USER, PASSWORD, HOSTNAME)) 
engine.execute("CREATE DATABASE IF NOT EXISTS %s "%(DATABASE)) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://%s:%s@%s/%s'%(USER, PASSWORD, HOSTNAME, DATABASE)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database migration command line
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


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

if __name__ == '__main__':
    manager.run()
