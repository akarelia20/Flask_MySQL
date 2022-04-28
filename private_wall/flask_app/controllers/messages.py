from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import message

@app.route("/message/delete/<int:id>", methods = ['POST'] )
def destory(id):
    data = {
        "id" : id
    }
    message.Message.delete(data)
    return redirect("/dashbord")