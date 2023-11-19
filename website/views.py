from flask import Blueprint, render_template, jsonify, request
import util, ExpenseTracker, User

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("landingPage.html")

@views.route("/input-income")
def income():
    return render_template("inputincomePage.html")

@views.route("/submitlogin", methods=['POST'])
def getLogin():
    usernameLogin = request.form['usernameLogin']
    passwordLogin = request.form['passwordLogin']

@views.route("/submitsignup", methods=['POST'])
def getSignup():
    usernameSignup = request.form['usernameSignup']
    passwordSignup = request.form['passwordSignup']

    # new_user, tracker = create(usernameLogin, passwordLogin)
    # new_user.save_to_file('user_data.json')
    # print("Sign Up Successful!")
    
    # try:
    #     existing_user = User.load_from_file('user_data.json')
    #     user = User(usernameSignup, passwordSignup)
    #     if user.login(usernameSignup, passwordSignup):
    #         # Perform actions after successful login if needed
    #         user.display_summary()
    #         # user.display_average_income()
    # except FileNotFoundError:
    #     print("No user data found. Please sign up first.")

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