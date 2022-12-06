# Melon Tasting Reservation App

## To Use: 

Test user login information: 
- test1_user = User(email="test1@test.test", username="test1", password=argon2.hash("test"))
- test2_user = User(email="test2@test.test", username="test2", password=argon2.hash("test"))
- test3_user = User(email="test3@test.test", username="test3", password=argon2.hash("test"))

## Technologies:

**Tech Stack:**
- Python
- HTML
- Flask
- Jinja
- PostgreSQL
- CSS
- Bootstrap

## Why I Chose the Technologies Used:

I used PostgreSQL because I wanted the users and data tied to those users to persist, so I needed a database. Furthermore, I used Python and the framework Flask to create the server. For the webpage, I used HTML and CSS for simple decorating, bootstrap for page layout, as well as Jinja for the templating power. 


## How I Structured My Database:

To structure my database, I created two tables: User and Appointments. I did it this way because I knew a user can have many appointments, but each individual appointment will only have one user. For the user, they have an id that auto-increments to keep track of each user, as well as an email, username, and password. They are connected to appointments via a middle table. Appointment contains appointment_id, appointment_date, appointment_start_time, appointment_end_time, and a foreign key to the user_id. 

I believe a potential tradeoff is having start time of the appointment separated from the appointment date (this could have been made into one). I did this however to add end_time to the database as well. I felt like it made sense if end_time was added to DB, then start time should be it's own category. 

## Extra Features:

- Password Hashing for login: I decided to implement passwords and password hashing for increased security for users who want to make melon reservations. 
- Cancel Reservation Button: Added a cancel reservation route so that users have the ability to delete unwanted reservations from their profile
- tests.py: I decided to add test to make sure the routes reroute correctly based on logged in vs not logged in users to ensure the web app was running properly. 