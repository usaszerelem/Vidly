To synchonize models with database
python3 manage.py makemigrations

To run all pending migrations on the database
python3 manage.py migrate

To run the server
python3 manage.py runserver

To create a default super user
python3 manage.py createsuperuser

To create a new app within the Python project. In this example 'api' app.
python3 manage.py startapp api

After creation of the app, it needs to be registered in the 'settings.py' file
in the INSTALLED_APPS section.
