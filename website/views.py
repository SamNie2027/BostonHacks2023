<<<<<<< HEAD
from flask import Blueprint, render_template, jsonify, request

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("landingPage.html")

@views.route("/input-income", method=['POST'])
def income():
    return render_template("inputincomePage.html")
def getUserPass():
    usernameLogin = request.form['usernameLogin']
    passwordLogin = request.form['passwordLogin']
    usernameSignup = request.form['usernameSignup']
    passwordSignup = request.form['passwordSignup']

@views.route("/input-expenses")
def expenses():
    return render_template("inputexpensesPage.html")

@views.route("/monthly-summary")
def summary():
    return render_template("monthlysummaryPage.html")

@views.route("/json")
def get_json():
    return jsonify({'name': 'jeff', 'coolness': 10})

@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)
=======
>>>>>>> parent of 571aaad (Completely implemented Python Flask)
