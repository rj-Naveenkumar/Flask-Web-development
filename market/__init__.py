from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy    #sqlite
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///market.db'
app.config['SECRET_KEY']='3b36d1bf226b6561392e838b'
db=SQLAlchemy(app)  #initialize instance for sql


from market import routes







