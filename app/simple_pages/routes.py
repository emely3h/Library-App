from flask import Blueprint, flash, redirect, url_for
from flask.templating import render_template

from flask_login import current_user
from flask_login import login_required

from app.authentication.models import User, Book, ReadingListItem, RentItem
from app.authentication.helpers.forms import BookForm
from app.extensions.authentication import login_manager
from datetime import datetime, timedelta

blueprint = Blueprint('simple_pages', __name__)

@blueprint.route("/", methods=['GET'])
def home():
    all_users = User.query.all()
    return render_template('index.html', users = all_users)

@blueprint.route('/admin')
def admin():
    form = BookForm()
    return render_template('simple_pages/admin.html', form = form)


@blueprint.route('/profile')
@login_required
def profile():
    rented_list = RentItem.query.filter_by(user_id = current_user.id).all()
    rented_books = []
    for item in rented_list:
        rented_books.append(Book.query.get(item.book_id))
    reading_list_items = ReadingListItem.query.filter_by(user_id = current_user.id).all()
    reading_list_books = []
    for item in reading_list_items:
        reading_list_books.append(Book.query.get(item.book_id))
    return render_template('simple_pages/profile.html', book_list = reading_list_books, rented_books_list = rented_books, rented_list= rented_list)

@blueprint.route('/books')
def books():
    books = Book.query.all()
    return render_template('simple_pages/books.html', books = books)

@blueprint.route('/add-book-to-bookshelf', methods=['POST'])
def add_book_to_bookshelf():
    form = BookForm()
    if form.validate_on_submit():
        book = Book(title = form.title.data, author = form.author.data, description = form.description.data, status = True)
        book.save()
        flash('The book has been added to the bookshelf.')
    return render_template('simple_pages/admin.html', form = form)

@blueprint.route('/add-book/<bookid>', methods=['POST'])
def add_book(bookid):
    form = BookForm()
    if form.validate_on_submit():
        book = Book(title = form.title.data, author = form.author.data, description = form.description.data, status = True)
        book.save()
        flash('The book has been added to the bookshelf.')
    return render_template('simple_pages/admin.html', form = form)

@blueprint.route('/book/<bookid>')
def book_details(bookid):
    book = Book.query.get(bookid)
    return render_template('simple_pages/book_details.html', book = book)

@blueprint.route('/dbschema')
def dbschema():
    return render_template('simple_pages/db-schema.html')


@blueprint.route('/add-to-reading-list/<bookid>', methods=['POST'])
@login_required
def addItemReadingList(bookid):
    readingListItem = ReadingListItem(user_id = current_user.id, book_id = bookid)
    readingListItem.save()
    flash('Book has been added')
    return redirect(url_for('simple_pages.books'))

@blueprint.route('/remove-from-reading-list/<bookid>', methods=['POST'])
@login_required
def removeItemReadingList(bookid):
    readingListItem = ReadingListItem.query.filter_by(user_id = current_user.id, book_id = bookid).first()
    readingListItem.delete()
    flash('Book has been removed')
    return redirect(url_for('simple_pages.profile'))

@blueprint.route('/rent-book/<bookid>', methods=['POST'])
@login_required
def rent_book(bookid):
    book = Book.query.get(bookid)
    book.change_status()
    rentItem = RentItem(user_id = current_user.id, book_id = bookid, start_date = datetime.now(), end_date = datetime.now() + timedelta(days=14))
    rentItem.save()
    flash('Book has been rented.')
    return redirect(url_for('simple_pages.profile'))

@blueprint.route('/return-book/<bookid>', methods=['POST'])
@login_required
def returnBook(bookid):
    returnItem = RentItem.query.filter_by(book_id = bookid, user_id = current_user)
    book = Book.query.get(bookid)
    book.change_status()
    returnItem.delete()
    flash('Book has been returned.')
    return redirect(url_for('simple_pages.profile'))