from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import user 
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods = ['POST'])
def register():
    if not user.User.validate_registration(request.form):
        return redirect("/")
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password" : pw_hash,
    }
    user_id = user.User.save(data) #method returns users.id from database
    # we are saving the user id in session so we can pull data
    session['user_id'] = user_id
    return redirect ("/dashbord")

@app.route("/login", methods= ['Post'])
def login():
    data = {
        "email": request.form['email']
    }
    # matches User from database(by email) and creates an instance of User class
    user_in_db = user.User.get_user_by_email(data)
    # if user_in_db is false then show flash message
    if not user_in_db: 
        flash("Invalid Email/Password !", "login")
        return redirect("/")
    # if we get False after checking the password
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Email/Password", "login")
        return redirect("/")
    # if user enters the correct combination of email/password on login 
    # user_id from "user_in_db" dictonary gets stored in session
    session['user_id'] = user_in_db.id
    return redirect("/dashbord")

@app.route("/dashbord")
def dashbord():
    if 'user_id' not in session:
        return redirect("/")
    data = {
        "id"  : session['user_id']
    }
    return render_template("dashbord.html",logged_in_user = user.User.get_user_by_id(data))

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")