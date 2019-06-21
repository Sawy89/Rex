# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 10:37:49 2019

App portale_rex

BIBLIO:
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-web-forms

DIPENDENZE:
pip install Flask
pip install flask-wtf
pip install flask-sqlalchemy
pip install flask-migrate
pip install flask-login

RUN:
set FLASK_APP=portale_rex.py
set FLASK_ENV=development
--> flask run
--> flask shell

@author: DT
"""

from app import app, db
from app.models import User, Post

@app.shell_context_processor
def make_shell_context():
    '''
    Importa automaticamente nella shell
    '''
    return {'db': db, 'User': User, 'Post': Post}

# MAIN per lanciarlo da spyder
if __name__ == "__main__":
#    app.debug = 5000
    app.run(debug=False, host='0.0.0.0', port=5000)