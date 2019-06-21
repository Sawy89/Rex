# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 11:29:15 2019

Classe di configurazione dell'applicazione

@author: DT
"""

import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    '''
    Classe di configurazione
    '''
    # secret key
    SECRET_KEY = os.environ.get('SECRET_KEY') or '42-is-the-answer'
    
    # DB setting
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False