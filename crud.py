"""CRUD operations."""

from model import db, User, Appointment, connect_to_db

from datetime import datetime, timedelta, time

def get_user_by_username(username):
    """Gets user by their username"""

    return User.query.filter(User.username == username).first()
    
def check_date_in_user_appts(date, user):
    """Checks to see if user already has an appointment on that date"""
    
    return Appointment.query.filter(Appointment.appointment_date == date, Appointment.user_id == user.user_id).first()

def get_all_taken_appts_start_time(date):
    """Gets all available appointments"""
    
    appts = Appointment.query.filter(Appointment.appointment_date == date).all()

    start_times = []

    for appt in appts: 
        start_times.append(appt.start_time)

    return start_times 

def get_all_appt_slots():
    """Returns a list of 30 minute intervals of a day"""

    return [time(t,m,0,0).strftime("%H:%M") for t in range(0, 24) for m in [0, 30]]

def create_appt(date, start_time, user):
    """Creates an appointment in the database for the user"""

    start_time_obj = datetime.strptime(start_time, "%H:%M")
    end_time = start_time_obj + timedelta(minutes=30)

    return Appointment(appointment_date=date, appointment_start_time=start_time_obj, appointment_end_time = end_time, user_id = user.user_id)

def get_users_appts_formatted(user):
    """Returns a dictionary with formatted datetime values to look like: {date: start_time, end_time}"""

    user_appt_info = {}

    user_appts = Appointment.query.filter(Appointment.user_id == user.user_id).all()

    for appt in user_appts:
        user_appt_info[appt.appointment_date.strftime("%x")] = [appt.appointment_start_time.strftime("%X"), appt.appointment_end_time.strftime("%X")]

    return user_appt_info

if __name__ == '__main__':
    from server import app
    connect_to_db(app)