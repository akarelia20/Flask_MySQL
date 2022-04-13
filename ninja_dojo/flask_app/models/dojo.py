from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    db = "dojo_and_ninjas_schema"
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(cls.db).query_db(query)
        dojos = []
        for row in results:
            dojos.append(cls(row)) # cls(row) is class-row each row in a table is an instance/object of this class 
        return dojos

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])
    
    @classmethod
    def get_ninjas(cls,data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results= connectToMySQL(cls.db).query_db(query, data)
        dojos = cls(results[0])
        for row_in_db in results:
            ninja_data = {
                "id" : row_in_db['ninjas.id'],
                "first_name" : row_in_db['first_name'],
                "last_name" :row_in_db['last_name'],
                "age" : row_in_db['age'],
                "created_at" :row_in_db['ninjas.created_at'],
                "updated_at" : row_in_db['ninjas.updated_at'],
                # "dojo_id": row_in_db['ninjas.dojo_id']
            }
            dojos.ninjas.append(ninja.Ninja(ninja_data))
        return dojos.ninjas
