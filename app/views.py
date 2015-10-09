from app import app, db
from flask import render_template, request, redirect, url_for
from app.models import Author, Book
from app.forms import AuthorForm, BookForm
from sqlalchemy import func, or_
from config import POSTS_PER_PAGE

@app.route('/', methods = ['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
@app.route('/index/<int:page>', methods = ['GET', 'POST'])
def index(page=1):    
    books = Book.query.join(Author).add_columns(
        Book.title, Book.year, Book.id, Author.name, Author.lastname).filter(
        Author.id == Book.author_id).paginate(page, POSTS_PER_PAGE, False)
    context = {'books': books,}
    return render_template('index.html', **context)


@app.route('/search/<search>')
def search(search): 
    if search.isdigit():
        books = Book.query.join(Author).add_columns(
            Book.title, Book.year, Book.id, Author.name, Author.lastname).filter(
            Author.id == Book.author_id).filter(
            Book.year == search).all()
    else:
        books = Book.query.join(Author).add_columns(
            Book.title, Book.year, Book.id, Author.name, Author.lastname).filter(
            Author.id == Book.author_id).filter(or_(
                Book.title.ilike('%{}%'.format(search)), 
                Author.name.ilike('%{}%'.format(search)), 
                Author.lastname.ilike('%{}%'.format(search)))).all()
    context = {'books': books, 'search': search}
    return render_template('searchresults.html', **context)


@app.route('/authors')
@app.route('/authors/<int:page>')
def authors(page=1):
    authors = Author.query.paginate(page, POSTS_PER_PAGE, False)
    return render_template('authors.html', authors=authors)


@app.route('/author/<id>')
def author(id):
    author = Author.query.get(id)
    form = AuthorForm(request.form, obj=author)
    return render_template('author.html', author=author, form=form)


@app.route('/addauthor', methods=['GET', 'POST'])
def addauthor():
    form = AuthorForm(request.form)
    if request.method == 'POST' and form.validate():
        user = Author(form.name.data, form.lastname.data,
                    form.born.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('authors'))
    return render_template('addauthor.html', form=form)


@app.route('/updateauthor', methods=['POST'])
def updateauthor():
    form = AuthorForm(request.form)
    author = Author.query.get_or_404(form.id.data)
    if request.method == 'POST':
        form.populate_obj(author)
        db.session.commit()
        return redirect(url_for('authors'))
    return render_template('error.html', form=form)

@app.route('/books/<id>')
def book(id):
    book = Book.query.filter_by(id=id).first()
    form = BookForm(request.form, obj=book)
    form.author_id.choices = [(i.id, i.lastname) for i in Author.query.all()]
    return render_template('book.html', book=book, form=form)


@app.route('/updatebook', methods=['POST'])
def updatebook():
    form = BookForm(request.form)
    form.author_id.choices = [(i.id, i.lastname) for i in Author.query.all()]
    book = Book.query.get_or_404(form.id.data)
    if request.method == 'POST' and form.validate():
        form.populate_obj(book)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('error.html', form=form)


@app.route('/addbook', methods=['GET', 'POST'])
def addbook():
    form = BookForm(request.form)
    form.author_id.choices = [(i.id, i.lastname) for i in Author.query.all()]
    if request.method == 'POST':
        book = Book(form.title.data, form.year.data,
                    form.author_id.data)
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('addbook.html', form=form)


@app.route('/<entity>/delete/<id>', methods=['POST'])
def delete(entity, id):
    if request.method == 'POST' and entity == 'book':
        book = Book.query.get(id)
        db.session.delete(book)
        db.session.commit()
        return redirect(url_for('index'))
    if request.method == 'POST' and entity == 'author':
        author = Author.query.get(id)
        db.session.delete(author)
        db.session.commit()
        return redirect(url_for('authors'))