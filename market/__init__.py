from flask import Flask
from flask_sqlalchemy import SQLAlchemy    #sqlite
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///market.db'
app.config['SECRET_KEY']='3b36d1bf226b6561392e838b'
db=SQLAlchemy(app)  #initialize instance for sql
bcrypt=Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login_page'
login_manager.login_message_category = 'info' 

from market import routes







