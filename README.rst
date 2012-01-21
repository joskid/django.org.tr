Requirements
============
You can install all Python dependencies with `pip install -r requirements.txt`.
We prefer you to use virtualenv. If you are developer, use
`requirements_dev.txt` instead.

Installation
============
Create settings/local.py file and write your settings to this file. Them, create
database tables with this command:

    python manage.py syncdb --migrate --noinput

If you need to a super user, create it with this command:

    python manage.py createsuperuser

Then create your `local_settings.py`. You can copy `local_settings.py-example`
file from repository. Always use your local_settings.py file, so start
development server as:

    python manage.py runserver_plus --settings=local_settings

Authors
-------
* Onur Mat, <omat_teknolab.org>
* Gökmen Görgen, <gokmen_alageek.com>