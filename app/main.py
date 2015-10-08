# -*- coding: utf-8 -*-

from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config.from_object('config')


@app.route('/')
def index():    
    books = ['January', 'February', ]
    author = {
        'January': {'author': "Stiven King", 'year': 1947, },
        'February': {'author': "Stiven King", 'year': 1951, },
    }
    return render_template('index.html', books=books,
                           author=author)

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {0}!</h1>'.format(name)

if __name__ == '__main__':
    app.run(debug=True, port=3000, host="0.0.0.0")