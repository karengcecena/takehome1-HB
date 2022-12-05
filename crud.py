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

    # reservation_times = [00:00, 24:00]
    # reservation_times_convert = sorted(datetime.strptime(x.encode('utf-8'),'%H:%M').time() for x in reservation_times)

    # return [time(t,m,0,0).strftime("%H:%M") for t in range(min(reservation_times).hour, max(reservation_times).hour) for m in [0, 30]]
    return [time(t,m,0,0).strftime("%H:%M") for t in range(0, 24) for m in [0, 30]]

if __name__ == '__main__':
    from server import app
    connect_to_db(app)