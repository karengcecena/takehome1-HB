"""CRUD operations."""

from model import db, User, Appointment, connect_to_db

def get_user_by_username(username):
    """Gets user by their username"""

    return User.query.filter(User.username == username).first()

def get_all_available_appts(date):
    """Gets all available appointments"""
    
    return Appointment.query.filter(Appointment.appointment_date == date).all()
    
def check_date_in_user_appts(date, user):
    """Checks to see if user already has an appointment on that date"""
    
    return Appointment.query.filter(Appointment.appointment_date == date, Appointment.user_id == user.user_id).first()

if __name__ == '__main__':
    from server import app
    connect_to_db(app)