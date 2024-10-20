# Welcome to Uranus educational website!

In order to activate the website, use the following steps:
1. Install PostgreSQL DBMS, and in pgAdmin, create a database
2. Download the project into your local environment
3. Open the folder "uranus" and make its content appear in your coding environment (it can be Visual Studio Code)
4. In your coding environment, find another folder called "uranus", and there find the file "settings.py"
5. In this file, find the folloing code and fill in with your own values

DATABASES = { 'default': { 'ENGINE': 'django.db.backends.postgresql', 'NAME': '{name of created database}', 'USER': '{your username on PostgreSQL DBMS}', 'PASSWORD': '{your passwrord registered when installing PostgreSQL DBMS}', 'HOST': '{name of the host (usually 'localhost')}', 'PORT': '{four digits of the port (usually '5432')}' } } These values can be found in connection string when clicking the server on the left side and navigating to properties on the right side of the program window.

In your coding environment, open the console terminal, and when you insert following commands one by one, don't forget to press Enter each time (this will be for Windows)

6. "cd ../"
7. ".\venv\Scripts\activate"
8. "cd uranus"
9. "py manage.py makemigrations"
10. "py manage.py migrate"
11. "py manage.py seed"
12. "py manage.py runserver"

After that the link to the website will appear. Open a browser and paste this link. You will see the whole website!
