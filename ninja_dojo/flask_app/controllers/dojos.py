from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo 

@app.route('/')
def index():
    return redirect('/dojos')

@app.route("/dojos")
def dojos():
    return render_template("dojos.html", dojos = Dojo.get_all())

# triggers when user adds a dojo , clicks submit
@app.route("/process_createdojo", methods = ['POST'])
def process_dojo():
    Dojo.save(request.form)
    return redirect ("/dojos")

@app.route("/get_ninjas/<int:id>")
def get_ninjas(id):
    data = {
        "id" : id
    }
    return render_template ("dojos_ninjas.html", ninjas = Dojo.get_ninjas(data), dojo= Dojo.get_one(data))
