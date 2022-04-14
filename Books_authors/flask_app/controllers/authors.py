from flask_app import app
from flask import render_template, redirect, request
from flask_app.models import author, book

@app.route("/")
def index():
    return redirect("/authors")

@app.route("/authors")
def display_authors():
    return render_template("authors.html", authors = author.Author.get_all())

@app.route("/author/create", methods = ['POST'])
def create_author():
    author.Author.save(request.form)
    return redirect ("/authors")

@app.route("/author/<int:id>")
def display_authorFav(id):
    data = {
        "id" : id
    }
    return render_template("author_fav.html", author = author.Author.get_one(data), author_books= author.Author.getAuthor_fav_books(data), books = book.Book.get_all())

@app.route("/author/add_fav", methods=['POST'])
def add_author_fav():
    data = {
        "book_id" : request.form['book_id'],
        "author_id" : request.form['author_id']
    } 
    author.Author.insert_favBooks(data)
    return redirect (f"/author/{request.form['author_id']}") # f-string only have one curly brackets" 

