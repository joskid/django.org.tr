Requirements
============
You can install all Python dependencies with `pip install -r requirements.txt`.
We prefer you to use virtualenv.

Installation
============
Create settings/local.py file and write your settings to this file. Them, create
database tables with this command:

    python manage.py syncdb --migrate --noinput

If you need to a super user, create it with this command:

    python manage.py createsuperuser
