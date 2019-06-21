# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 10:43:02 2019

Pagine dell'applicazione

@author: DT
"""
from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

from app import app, db
from app.forms import LoginForm, RegistrationForm
from app.models import User


@app.route('/')
@app.route('/index')
@login_required
def index():
    '''
    pagina index
    '''
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home Page', posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    '''
    pagina di login: se ha fatto il login, rimanda alla pagina di index
    '''
    # Se l'utente è già registrato, rimanda all'index
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    # crea la form
    form = LoginForm()
    
    # Se la form è stata inserita: login fatto
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        # Login fallito: nuovamente alla pagina di login
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        # Login successo: se presente, redirect alla pagina a cui si era tentato di accedere
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    
    # Se la form non è stata compilata: pagina di login
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    '''
    pagina per il logout dalla sessione
    '''
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    '''
    Pagina di registrazione di un nuovo utente
    '''
    # Se l'utente è già registrato, rimanda all'index
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    # crea la form
    form = RegistrationForm()
    
    # Se la form è stata inserita: carico il nuovo utente su DB
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    
    # Se la form non è stata compilata: form di registrazione
    return render_template('register.html', title='Register', form=form)    