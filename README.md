# juancruzcrotta.github.io
Installation Guide:
Set up a virtual environment.
Change directories into the root of the project and install the project requirements: pip install -r requirements.txt
Either add environment variables to your system for SECRET_KEY and DEBUG or set them yourself. They should work without any additional work but it's best to have control of everything if possible.
Decide if you want django-storages and django-heroku and set up their variables in portfolio/settings.py accordingly if so or remove them if not.
Install migrations to your database using python manage.py migrate
Create a superuser to get into the admin panel. python manage.py createsuperuser
Go to your admin panel (should be at http://127.0.0.1:8000/admin/)
Set up your objects to fill in the site in the proper locations and they'll automatically display on the home page. http://127.0.0.1:8000/admin/
For the "Social" section there are preloaded icons you can use in the portfolio\website\static\website\img folder. This should get you started.
Have fun :-)
