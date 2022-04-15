from flask_app import app
from flask_app.models import dojo
from flask import render_template, request, redirect

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    if not dojo.Dojo.validate_form(request.form):
        return redirect("/")
    dojo.Dojo.save(request.form)
    return redirect("/results" )

@app.route('/results')
def results():
    return render_template("results.html", last_survey= dojo.Dojo.get_last_survey())


