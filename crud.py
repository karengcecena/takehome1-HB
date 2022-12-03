"""CRUD operations."""

from model import db, User, Appointment, connect_to_db

def get_user_by_username(username):
    """Gets user by their username"""

    return User.query.filter(User.username == username).first()

if __name__ == '__main__':
    from server import app
    connect_to_db(app)