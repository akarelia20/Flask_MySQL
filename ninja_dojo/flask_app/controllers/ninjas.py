from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/ninjas')
def ninjas():
    return render_template("ninjas.html", dojos= Dojo.get_all())

@app.route('/process_createninja', methods = ['POST'])
def process_ninja():
    Ninja.save(request.form)
    return redirect('/')