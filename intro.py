from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello wolrd</h1>'

@app.route('/about')
def about():
    return '<h1>About page</h1>'

@app.route('/about/<username>')   # dynamic route
def about_page(username):
    return f'<h1>Hello this is {username}!</h1>' 




if __name__ == '__main__':
    app.run(debug=True)