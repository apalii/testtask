#from flask.ext.wtf import Form
from wtforms import Form, TextField, IntegerField, HiddenField, SelectField
from wtforms.validators import Length, Required
from app.models import Author, Book

class AuthorForm(Form):
    id = HiddenField()
    name = TextField('Name', [Length(min=3, max=25), Required()])
    lastname = TextField('Lastname', [Length(min=4, max=25), Required()])
    born = IntegerField('Year of born', [Required()])


class BookForm(Form):
    id = HiddenField()
    title = TextField('Title', [Length(min=2, max=55), Required()])
    year = IntegerField('Year', [Required()])
    author_id = SelectField(coerce=int)
    
