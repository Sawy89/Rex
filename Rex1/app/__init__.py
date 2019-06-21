# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 16:31:11 2019

Init dell'applicazione:
importa Flask, la classe di configurazione e le funzioni dell'app

@author: DT
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

from app.config import Config

# Istanza dell'applicazione
app = Flask(__name__)
app.config.from_object(Config)

# Istanze di database, migrazione del database e login
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)

# Indicazione della pagina di login
login.login_view = 'login' # indicata come in url_for

# import delle pagine e dei modelli
from app import routes, models