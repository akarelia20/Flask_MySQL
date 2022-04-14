from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book

class Author:
    db = "books_schema"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.books = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors;"
        results = connectToMySQL(cls.db).query_db(query)
        authors = []
        for row in results:
            authors.append(cls(row)) # cls(row) is class-row each row in a table is an instance/object of this class 
        return authors

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM authors WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls,data):
        query = "INSERT INTO authors (name) VALUE (%(name)s); "
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def getAuthor_fav_books(cls,data):
        query = "SELECT * FROM authors LEFT JOIN favorites ON authors.id = favorites.author_id LEFT JOIN books ON favorites.book_id = books.id WHERE authors.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        authors = cls(results[0])
        for row_in_db in results:
            book_data = {
                "id" : row_in_db['books.id'],
                "title": row_in_db['title'],
                "num_of_pages": row_in_db['num_of_pages'],
                "created_at": row_in_db['books.created_at'],
                "updated_at": row_in_db['updated_at']
            }
            authors.books.append(book.Book(book_data))
        print(authors.books)
        return authors.books

    @classmethod
    def insert_favBooks(cls,data):
        query = "INSERT INTO favorites (author_id, book_id) VALUES (%(author_id)s, %(book_id)s);"
        return connectToMySQL(cls.db).query_db(query,data)

