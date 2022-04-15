from unittest import result
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Dojo:
    db = "dojo_survey_schema"
    def __init__(self,data):
        self.id = data["id"]
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO dojos (name, location, language, comment) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s);"
        return connectToMySQL(cls.db). query_db(query,data)
    
    @classmethod
    def get_last_survey(cls):
        query = "SELECT * FROM dojos ORDER BY dojos.id DESC LIMIT 1;"
        result = connectToMySQL(cls.db).query_db(query)
        print(result)
        return Dojo(result[0]) 
    
    @staticmethod
    def validate_form(form):
        is_valid = True
        if len(form['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(form['location']) <= 0:
            flash("You must select location to proceed")
            is_valid = False
        if len(form['language']) <= 0:
            flash("You must select language to proceed")
            is_valid = False
        if len(form['comment']) < 3:
            flash("Comments must be at least 3 characters")
            is_valid = False
        return is_valid



