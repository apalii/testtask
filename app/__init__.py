from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bootstrap import Bootstrap
from flask_wtf.csrf import CsrfProtect


app = Flask(__name__)
CsrfProtect(app)
bootstrap = Bootstrap(app)
app.config.from_object('config')
db = SQLAlchemy(app)

from app import views, models

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')