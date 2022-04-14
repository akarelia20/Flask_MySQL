from flask_app import app
from flask import render_template, redirect, request
from flask_app.models import author, book

@app.route("/books")
def display_books():
    return render_template("books.html", books = book.Book.get_all())

@app.route("/book/create", methods = ['POST'])
def create_book():
    book.Book.save(request.form)
    return redirect ("/books")

@app.route("/book/<int:id>")
def display_favBy(id):
    data = {
        "id" : id
    }
    return render_template("book_fav.html", book = book.Book.get_one(data), faviorited_by_authors = book.Book.get_authors(data), authors = author.Author.get_all())

@app.route("/book/add_fav", methods=['POST'])
def add_book_fav():
    data = {
        "book_id" : request.form['book_id'],
        "author_id" : request.form['author_id']
    } 
    author.Author.insert_favBooks(data)
    return redirect (f"/book/{request.form['book_id']}") # f-string only have one curly brackets" 

