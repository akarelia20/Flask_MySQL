from crypt import methods
from flask_app import app
from flask import render_template, redirect, request, flash
from flask_app.models import email

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/create", methods =["POST"])
def create():
    if email.Email.form_validation(request.form) == False:
        return redirect("/")
    email.Email.save(request.form)
    # if not id :
    #     flash('Something got messed up somewhere')
    #     return redirect('/')
    return redirect("/dashbord")

@app.route("/dashbord")
def show_all_email():
    return render_template ("sucess_page.html", emails_from_db = email.Email.get_all_emails())

@app.route("/destroy/<int:id>")
def destroy(id):
    data = {
        "id" : id
    }
    email.Email.delete(data)
    return redirect("/dashbord")