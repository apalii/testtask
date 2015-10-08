from wtforms import Form, TextField, IntegerField, HiddenField, SelectField
from wtforms.validators import Length, Required
from app.models import Author, Book

class AuthorForm(Form):
    id = HiddenField()
    name = TextField('Name', [Length(min=3, max=25)])
    lastname = TextField('Lastname', [Length(min=4, max=25)])
    born = TextField('Year of born', [Length(min=4, max=4)])


class BookForm(Form):
    id = HiddenField()
    title = TextField('Title', [Length(min=2, max=55)])
    year = TextField('Year', [Length(min=4, max=25)])
    author_id = SelectField(u"Author", [Required()])
    
