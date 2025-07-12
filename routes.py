from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy    #sqlite
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///market.db'
db=SQLAlchemy(app)  #initialize instance for sql

class Item(db.Model):
    id=db.Column(db.Integer(), primary_key=True)
    name=db.Column(db.String(length=30), nullable=False, unique=True)
    price=db.Column(db.String(), nullable=False)
    barcode=db.Column(db.String(length=12), nullable=False, unique=True)
    description=db.Column(db.String(length=1024), nullable=False, unique=True)


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items=[
        {'id':1,'name':'phone','price':350000},
        {'id':2,'name':'laptop','price':500000},
        {'id':3,'name':'tablet','price':200000},
    ]
    return render_template('market.html',items=items)

if __name__ == '__main__':
    app.run(debug=True)
