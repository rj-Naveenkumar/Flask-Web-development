from flask import Flask,render_template
app=Flask(__name__)

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
