# -*- coding: utf-8 -*-

from flask import Flask, render_template, json, request, session, redirect, url_for, flash
from web import app, db
from model import User

db.init_app(app)

db.create_all()

app.secret_key = 'secret_key'

@app.route("/")
def main():
    return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/showSignIn')
def showSignIn():
    return render_template('signin.html')

@app.route('/signUp', methods=['POST', 'GET'])
def signUp():

    try:
        
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']
        _name = request.form['inputName']
        _surname = request.form['inputSurname']

        sql = User.query.filter_by(email=_email).first()

        if sql is None: 

            db.session.add(User(email=_email,password= _password, name=_name, surname=_surname, visit=0))
            db.session.commit()

            return render_template('index.html')
        
        else:

            return render_template('error.html', error='mail non disponibile')
        
    except Exception as e:
        
        return render_template('error.html', error=json.dumps({'error':str(e)})) 
        
@app.route('/signIn', methods=['POST'])
def signIn():

    try:
        
        _email = request.form['inputEmail']
        _password = request.form['inputPassword'] 
            
        sql = User.query.filter_by(email=_email, password=_password).first()

        if sql is not None: 
            
            sql.visit = sql.visit + 1
            db.session.commit()

            session['username'] = _email
            
            return render_template('welcomeUser.html', name=sql.name, surname=sql.surname, visit=sql.visit) 
        
        else:

            return render_template('error.html', error='utente non registrato')

    except Exception as e:

        return render_template('error.html', error=json.dumps({'error':str(e)}))

@app.route('/signOut')
def logout():
   session.pop('username', None)
   return redirect('/')

