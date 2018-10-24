from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand



# Database Configurations
app = Flask(__name__)
DATABASE = 'AppDB'
PASSWORD = 'root'
USER = 'root'
HOSTNAME = 'mysqlserver'


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://%s:%s@%s/%s'%(USER, PASSWORD, HOSTNAME, DATABASE)
db = SQLAlchemy(app)

# Database migration command line
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

class User(db.Model):

    # Data Model User Table
    email = db.Column(db.String(45), primary_key=True)
    password = db.Column(db.String(45), unique=False)
    name = db.Column(db.String(45), unique=False)
    surname = db.Column(db.String(45), unique=False)
    visit = db.Column(db.Integer, unique=False)
    
    def __init__(self, name, email, password, surname, visit):
        # initialize columns
        self.name = name
        self.email = email
        self.password = password
        self.surname = surname
        self.visit = visit

    def __repr__(self):
        return '<User %r>' % self.name

class CreateDB():
    def __init__(self, hostname=None):
        import sqlalchemy
        engine = sqlalchemy.create_engine('mysql://%s:%s@%s'%(USER, PASSWORD, HOSTNAME)) # connect to server
        engine.execute("CREATE DATABASE IF NOT EXISTS %s "%(DATABASE)) #create db

if __name__ == '__main__':
    manager.run()
