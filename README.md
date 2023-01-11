## ChatApp

The first thing to do is to clone the repository:

$ git clone https://github.com/maulikkanani2/ChatApp.git
$ cd ChatApp
Create a virtual environment to install dependencies in and activate it:

$ python3 -m venv venv
$ source venv/bin/activate
Then install the dependencies:

(venv)$ pip install -r requirements.txt
Note the (venv) in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by virtualenv2.

Once pip has finished downloading the dependencies:

# create database
- open psql terminal
$ sudo -u postgres psql
- create database
postgres=# CREATE DATABASE chatapp;


# database migrations
(venv)$ python manage.py makemigrations
(venv)$ python manage.py migrate

# for create superuser(admin)
(venv)$ python manage.py createsuperuser

# run project
(venv)$ python manage.py runserver


Login URL ==> http://127.0.0.1:8000/login/