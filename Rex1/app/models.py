# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 14:38:22 2019

Lista delle tabelle database

@author: DT
"""

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

from app import db, login


class User(UserMixin, db.Model):
    '''
    tabella con gli utenti registrati
    '''
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic') # link per join

    def __repr__(self):
        '''
        Print quando viene chiamata l'istanza
        '''
        return '<User {}>'.format(self.username)
    
    def set_password(self, password):
        '''
        Funzione per salvare il password_hash a partire dalla password 
        (la password non viene MAI salvata su DB!)
        '''
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        '''
        Funzione per verificare se la password inserita è corretta
        '''
        return check_password_hash(self.password_hash, password)
        

class Post(db.Model):
    '''
    Tabella con i post
    '''
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        '''
        Print quando viene chiamata l'istanza
        '''
        return '<Post {}>'.format(self.body)


@login.user_loader
def load_user(id):
    '''
    Funzione per comunicare a flask qual è lo user se forniamo un id
    '''
    return User.query.get(int(id))