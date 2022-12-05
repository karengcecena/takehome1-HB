# Melon Tasting Reservation App

## Technologies

**Tech Stack:**
- Python
- HTML
- Javascript
- Flask
- Jinja
- PostgreSQL
- CSS
- Bootstrap

## Why I chose the technologies used



## How you structured your database

To structure my database, I created two tables: User and Appointments. I did it this way because I knew a user can have many appointments, but each individual appointment will only have one user. For the user, they have an id that auto-increments to keep track of each user, as well as an email, username, and password. They are connected to appointments via a middle table. Appointment contains appointment_id, appointment_date, appointment_start_time, appointment_end_time, and a foreign key to the user_id. 

I believe a potential tradeoff is having start time of the appointment separated from the appointment date (this could have been made into one). I did this however to add end_time to the database as well. I felt like it made sense if end_time was added to DB, then start time should be it's own category. 

## Extra Features

- Password Hashing for login. I decided to implement passwords and password hashing for increased security for users who want to make melon reservations. 