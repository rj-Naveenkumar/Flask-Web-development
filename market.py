from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy    #sqlite
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///market.db'


import models
import routes



if __name__ == '__main__':
    app.run(debug=True)
