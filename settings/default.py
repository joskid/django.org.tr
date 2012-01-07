#-*- coding: utf-8 -*-
from os import path

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    (u'Onur Mat', 'omat@teknolab.org'),
    (u'Gokmen Gorgen', 'gokmen@alageek.com')
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'sqlite.db'
    }
}

SECRET_KEY = 'please-generate-your-secret-key'
SUPERFEEDR_LOGIN = ('my_superfeedr_username', 'password')

ROOT = path.split(path.realpath(path.dirname(__file__)))[0]

MEDIA_ROOT = ''
STATIC_ROOT = path.join(ROOT, '.epio_static')
STATICFILES_DIRS = (path.join(ROOT, 'static'),)

# TWITTER_CONSUMER_KEY = ''
# TWITTER_CONSUMER_SECRET = ''
FACEBOOK_APP_ID = ''
FACEBOOK_API_SECRET = ''
# LINKEDIN_CONSUMER_KEY = ''
# LINKEDIN_CONSUMER_SECRET = ''
# ORKUT_CONSUMER_KEY = ''
# ORKUT_CONSUMER_SECRET = ''
GOOGLE_CONSUMER_KEY = ''
GOOGLE_CONSUMER_SECRET = ''
# GOOGLE_OAUTH2_CLIENT_ID = ''
# GOOGLE_OAUTH2_CLIENT_SECRET = ''
# FOURSQUARE_CONSUMER_KEY = ''
# FOURSQUARE_CONSUMER_SECRET = ''
# GITHUB_APP_ID = ''
# GITHUB_API_SECRET = ''
# DROPBOX_APP_ID = ''
# DROPBOX_API_SECRET = ''
# FLICKR_APP_ID = ''
# FLICKR_API_SECRET = ''
