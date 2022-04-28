from email import message
from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask import flash
from flask_app.models import user
from datetime import datetime
import math

class Message:
    db = 'private_wall'
    def __init__(self, data):
        self.id = data['id']
        self.users_id = data['users_id']
        self.reciever_id = data['reciever_id']
        self.message = data['message']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.sender = None
        # self.results = []

    def time_delta(self):
        now = datetime.now()
        delta = now - self.created_at
        if delta.days > 0:
            return f"{delta.days} days ago"
        elif (math.floor(delta.total_seconds() / 60)) >= 60:
            return f"{math.floor((delta.total_seconds() / 60)/60)} hours ago"
        elif delta.total_seconds() >= 60:
            return f"{math.floor(delta.total_seconds() / 60)} minutes ago"
        else:
            return f"{math.floor(delta.total_seconds())} seconds ago"

    @classmethod
    def save_message(cls,data):
        query = "INSERT INTO messages (users_id, reciever_id , message) VALUES (%(users_id)s, %(reciever_id)s, %(message)s);"
        return MySQLConnection(cls.db).query_db(query,data)

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM messages where id = %(id)s;"
        return MySQLConnection(cls.db).query_db(query,data)
    