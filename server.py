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

            return redirect("/search_appt")
        
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
        flash("Sorry. You must log in to reserve for melon tasting.")
        return redirect("/")

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
        flash("Sorry, you already have a reservation scheduled for that day")
        return redirect("/search_appt")

    else: 
        taken_start_times = crud.get_all_taken_appts_start_time(date)
        taken_start_times_set = set(taken_start_times)

        all_app_slots = crud.get_all_appt_slots()

        all_available_reservations = []

        # to filter appointments already taken (by start time)
        for slot in all_app_slots:
            if slot not in taken_start_times_set:
                all_available_reservations.append(slot)

        all_available_reservations_within_times = []

        # to filter appointments if start and end time were given:
        if start_time:
            if end_time:
                for slot in all_available_reservations:
                    if slot >= start_time and slot <= end_time:
                        all_available_reservations_within_times.append(slot)
            else:
                flash("Make sure to put both start and end time in if you want to limit time search")

        else: 
            all_available_reservations_within_times.extend(all_available_reservations)

        return render_template("search_appt_results.html", date=date, all_available_reservations_within_times=all_available_reservations_within_times)

@app.route("/create_appt", methods=["POST"])
def create_appt():
    """Creates an appt for user"""

    user_username =  session["username"]
    user = crud.get_user_by_username(user_username)

    appt_start_time = request.form.get("start_time")
    date = request.form.get("date")

    appt = crud.create_appt(date, appt_start_time, user)

    db.session.add(appt)
    db.session.commit()

    return redirect("/profile")

@app.route("/cancel_reservation", methods=["POST"])
def delete_reservation():
    """Deletes Selected Reservation for User"""

    user_username =  session["username"]
    user = crud.get_user_by_username(user_username)

    appt_date = request.form.get("date")

    appt = crud.check_date_in_user_appts(appt_date, user)

    db.session.delete(appt)
    db.session.commit()

    return redirect("/profile")

@app.route("/profile")
def user_profile():
    """View user profile with scheduled appts"""

    if not "username" in session:
        flash("Sorry. You must log in to reserve for melon tasting.")
        return redirect("/")
    
    user_username =  session["username"]
    user = crud.get_user_by_username(user_username)

    appts = crud.get_users_appts_formatted(user)

    return render_template("scheduled_appts.html", user=user, appts=appts)

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
    app.run()