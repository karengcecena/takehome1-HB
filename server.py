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
    """Display's page for search feature of schedule appt"""

    if "username" in session:
        return render_template("search_appt.html")

    else: 
        return redirect("/login")

@app.route("/display_appts_available", methods=["POST"])
def display_appts():
    """Display's page with all appts available"""

    date = request.form.get("reservation_date")
    start_time = request.form.get("start_time")
    end_time = request.form.get("end_time")

    user_username =  session["username"]
    user = crud.get_user_by_username(user_username)

    #if date in users appts already:
    if crud.check_date_in_user_appts(date, user):
        flash("Sorry, you already have an appt scheduled for that day")
        return redirect("/search_appt")

    else: 
        taken_appts = crud.get_all_available_appts(date)
        return render_template("search_appt_results.html", taken_appts=taken_appts, start_time=start_time, end_time=end_time)

@app.route("/profile")
def user_profile():
    """View user profile with scheduled appts"""
    
    user_username =  session["username"]
    user = crud.get_user_by_username(user_username)

    return render_template("scheduled_appts.html", user=user)

@app.route("/logout")
def logout():
    """Log user out by clearing the session"""
    
    if "username" in session: 
        session.clear()
        flash("You've been logged out")
    else:
        flash("Sorry, please log in:")
    
    return redirect("/")

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)