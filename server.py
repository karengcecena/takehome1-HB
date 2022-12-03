from flask import (Flask, render_template, request, flash, session, redirect)

from jinja2 import StrictUndefined


app = Flask(__name__)
app.secret_key = "session_secret"
app.jinja_env.undefined = StrictUndefined

@app.route("/")
def homepage():
    """View login page"""

    return render_template("login.html")

@app.route("/login")
def login():
    """Logs user in"""

    return redirect("/schedule_appt")

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
    app.run(debug=True, host='0.0.0.0')