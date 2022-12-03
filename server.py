from flask import (Flask, render_template, request, flash, session, redirect)
from jinja2 import StrictUndefined
from model import connect_to_db, db
import crud

# import for hashing passwords
from passlib.hash import argon2


app = Flask(__name__)
app.secret_key = "session_secret"
app.jinja_env.undefined = StrictUndefined

@app.route("/")
def homepage():
    """View login page"""

    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    """Logs user in"""

    username = request.form.get("username")
    password = request.form.get("password")
    user = crud.get_user_by_username(username)

    if user:
        if argon2.verify(password, user.password):
            session["username"] = user.username

            return redirect("/schedule_appt")
        
        else:
            flash("Your password was incorrect. Please try again.")

    else:
        flash("Sorry, a user with that email doesn't exist")
    
    return redirect("/login")

@app.route("/search_appt")
def show_schedule_appt():
    """Display's page to schedule appt"""

    return render_template("search_appt.html")

@app.route("/schedule_appt")
def schedule_appt():
    """Display's page to schedule appt"""

    return render_template("search_appt.html")

@app.route("/profile")
def user_profile():
    """View user profile with scheduled appts"""

    return render_template("scheduled_appts.html")

@app.route("/logout")
def logout():
    """Log user out"""

    return redirect("/")

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)