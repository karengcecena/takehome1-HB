"""Models for Melon Reservation App """

from flask_sqlalchemy import SQLAlchemy

# import for hashing passwords
from passlib.hash import argon2

db = SQLAlchemy()

class User(db.Model):
    """User information"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String())

    # middle table: 
    appointments = db.relationship('Appointment', back_populates="user")

    def __repr__(self):
        """Show info about User"""

        return f"<User user_id = {self.user_id} username = {self.username} email = {self.email}>"

class Appointment(db.Model):
    """Appointment information"""

    __tablename__ = "appointments"

    appointment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    appointment_date = db.Column(db.DateTime, nullable=False)
    appointment_start_time = db.Column(db.DateTime, nullable=False)
    appointment_end_time = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)

    # middle table: 
    user = db.relationship('User', back_populates="appointments")

    def __repr__(self):
        """Show info about the Appointment"""

        return f"<Appointment appointment_id: {self.appointment_id} appointment_date: {self.appointment_date} appointment_start_time: {self.appointment_start_time} appointment_end_time: {self.appointment_end_time}>"

def connect_to_db(flask_app, db_uri="postgresql:///melon_tasting_db", echo=True):
    """Connect to database."""

    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Successfully connected to DB")

def example_data():
    """Create some sample data for testing."""

    # In case this is run more than once, empty out existing data
    User.query.delete()

    # Add sample users
    example_testpy1 = User(email="testpy1@test.com", username="testpy1" , password=argon2.hash("test"))
    example_testpy2 = User(email="testpy2@test.com", username="testpy2" , password=argon2.hash("test"))
    example_testpy3 = User(email="testpy3@test.com", username="testpy3" , password=argon2.hash("test"))

    db.session.add_all([example_testpy1, example_testpy2, example_testpy3])
    db.session.commit()

if __name__ == "__main__":
    from server import app
    
    connect_to_db(app)
    db.create_all()
    