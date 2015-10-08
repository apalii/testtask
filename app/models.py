# -*- coding: utf-8 -*-
from app import db
"""
>>> from app.models import Book
>>> from app.models import Author
>>> Book.query.all()
[]
>>> author = Author(name="King", born="1965")
>>> author
Authr: King id : None
>>> db.session.add(author)
>>> db.session.commit()
>>> Author.query.all()
[Authr: King id : 1]
"""
class Author(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20))
    lastname = db.Column(db.String(20))
    born = db.Column(db.String(4))
    
    def __init__(self, name, lastname, born):
        self.name = name
        self.lastname = lastname
        self.born = born
        
    def __repr__(self):
        return 'Author: {} {} id : {}'.format(self.name, self.lastname, self.id)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(40))
    year = db.Column(db.String(4))
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    
    def __init__(self, title, year, author_id):
        self.title = title
        self.year = year
        self.author_id = author_id
        
    def __repr__(self):
        return '<Book: %r>' % (self.title)