from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
class Email:
    db = "email_validation"
    def __init__(self,data):
        self.id = data["id"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def save(cls,data):
        query = "INSERT INTO emails (email) VALUE (%(email)s);"
        return MySQLConnection(cls.db).query_db(query,data)
    
    @classmethod
    def get_all_emails(cls):
        query = "SELECT * FROM emails"
        results = MySQLConnection(cls.db).query_db(query)
        list_of_emails = []
        for row in results:
            list_of_emails.append(cls(row))
        return list_of_emails

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM emails WHERE id = %(id)s;"
        return MySQLConnection(cls.db).query_db(query,data)

    @staticmethod
    def form_validation(form):
        is_valid = True
        query = 'SELECT * FROM emails WHERE email = %(email)s;'
        results = connectToMySQL(Email.db).query_db(query, form)
        print(results)
        if len(results) >= 1:
            flash("This email is already in our database")
            is_valid = False
        elif EMAIL_REGEX.match(form['email']):
            flash("Email address you enterd is valid!!")
            is_valid= True
        if not EMAIL_REGEX.match(form['email']):
            flash("Invalid email address!")
            is_valid = False
        return is_valid

