from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy

def create_app(test_config=None, db_path=None):
   
    app = Flask(__name__)

    DATABASE = 'AppDB'
    PASSWORD = 'root'
    USER = 'root'
    HOSTNAME = 'database'

    #engine = sqlalchemy.create_engine('mysql://%s:%s@%s'%(USER, PASSWORD, HOSTNAME)) 

    if test_config:

        app.config.update(test_config)
        DATABASE = db_path
        engine = sqlalchemy.create_engine('mysql://%s:%s@%s'%(USER, PASSWORD, HOSTNAME))
        engine.execute("CREATE DATABASE IF NOT EXISTS %s "%(DATABASE))
        engine.execute("INSERT INTO User (email, password, name, surname, 1) VALUES ('prova1@gmail.com', '123', 'prova1', 'cognome1', 1)")
        engine.execute("INSERT INTO User (email, password, name, surname, 1) VALUES ('prova2@gmail.com', '1', 'prova2', 'cognome2', 5)")
        engine.execute("INSERT INTO User (email, password, name, surname, 1) VALUES ('prova3@gmail.com', '3', 'prova3', 'cognome3', 32)")
        engine.execute("INSERT INTO User (email, password, name, surname, 1) VALUES ('prova4@gmail.com', '2', 'prova4', 'cognome4', 1)")
   
    else:
        engine = sqlalchemy.create_engine('mysql://%s:%s@%s'%(USER, PASSWORD, HOSTNAME))
        engine.execute("CREATE DATABASE IF NOT EXISTS %s "%(DATABASE))
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://%s:%s@%s/%s'%(USER, PASSWORD, HOSTNAME, DATABASE)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 


    return app

def init_db(app):

    db = SQLAlchemy(app)

    #db.init_app(app)

    #db.create_all()

    return db

app = create_app()
db = init_db(app)

from web import routes


