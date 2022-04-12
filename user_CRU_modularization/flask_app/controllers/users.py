from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.user import User

@app.route("/")
def home():
    return redirect("/users")

@app.route("/users")
def user():
    users = User.get_all()
    return render_template ("read_all.html", users= users)

@app.route("/users/new")
def create_user():
    return render_template("create.html")

@app.route("/users/create", methods= ['POST'])
def add_user():
    data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    User.save(data)
    return redirect("/users")

@app.route("/users/<int:id>")
def show(id):
    data = {
        "id" : id
    }
    return render_template("display_user.html", user = User.show(data) )

@app.route("/users/edit/<int:id>")
def edit(id):
    data = {
        "id" : id
    }
    return render_template("edit_user.html", user = User.show(data))

@app.route("/users/update", methods=['POST'])
def update():
    User.update(request.form)
    return redirect("/users")

@app.route("/users/delete/<int:id>")
def delete(id):
    data = {
        "id" : id
    }
    User.delete(data)
    return redirect("/users")