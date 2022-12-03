from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """User information"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String())
    appointment_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)

    # middle table: 
    appointments = db.relationship('Appointment', back_populates="user")

    def __repr__(self):
        """Show info about User"""

        return f"<User user_id = {self.user_id} username = {self.username} email = {self.email}>"

class Appointment(db.Model):
    """Appointment information"""

    __tablename__ = "appointments"

    appointment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    appointment_start_time = db.Column(db.DateTime)
    appointment_end_time = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)

    # middle table: 
    user = db.relationship('User', back_populates="appointments")

    def __repr__(self):
        """Show info about the Appointment"""

        return f"<Media appointment_id: {self.appointment_id} appointment_start_time: {self.appointment_start_time} appointment_end_time: {self.appointment_end_time}>"

def connect_to_db(app, db_uri="postgresql:///project_db", echo=True):
    """Connect to database."""

    app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    app.config["SQLALCHEMY_ECHO"] = True
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = app
    db.init_app(app)

if __name__ == "__main__":
    from server import app
    connect_to_db(app)
    db.create_all()