Mongo-Login-Auth Example
=========================================

Just a login auth with Mongo and Django

How to use it
-------------

In the toplevel directory of the project there is a requirements.txt file with all the python dependencies, required for this project to run. Install them with

`pip install -r requirements.txt`

After that you'll need to create a database in MongoDB, called `project`, where this project's collections will be stored.

To run this project with django development server, just go to `project` folder and say:

`python manage.py runserver`

and visit http://localhost:8000/api/ url, where you'll find the root of your REST api.


{
    "user": "http://127.0.0.1:8000/api/user/",
    "users": "http://127.0.0.1:8000/api/users/",
    "auth": "http://127.0.0.1:8000/api/auth/"
}

