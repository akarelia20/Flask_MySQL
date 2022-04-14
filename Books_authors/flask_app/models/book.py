from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author

class Book:
    db = "books_schema"
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.authors = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL(cls.db).query_db(query)
        books = []
        for row in results:
            books.append(cls(row)) # cls(row) is class-row each row in a table is an instance/object of this class 
        print(books)
        return books

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM books WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls,data):
        query = "INSERT INTO books (title, num_of_pages) VALUE (%(title)s, %(num_of_pages)s); "
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_authors(cls,data):
        query = "SELECT * FROM books LEFT JOIN favorites ON books.id = favorites.book_id LEFT JOIN authors ON favorites.author_id = authors.id WHERE books.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        books = cls(results[0])
        for row_in_db in results:
            author_data = {
                "id" : row_in_db['authors.id'],
                "name": row_in_db['name'],
                "created_at": row_in_db['authors.created_at'],
                "updated_at": row_in_db['authors.updated_at']
            }
            books.authors.append(author.Author(author_data))
        return books.authors



