# -*- coding: utf-8 -*-
from os import path
from local_settings import *

SITE_ROOT = path.realpath(path.dirname(__file__))
TEMPLATE_DIRS = (path.join(SITE_ROOT, 'templates'),)

MEDIA_ROOT = path.join(SITE_ROOT, 'static')
MEDIA_URL = '/'

TIME_ZONE = 'Europe/Istanbul'

LANGUAGE_CODE = 'tr'

SITE_ID = 1

DEFAULT_FROM_EMAIL = 'Django <django@django.org.tr>'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_SUBJECT_PREFIX = '[django-tr] '


# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'f_=farowr+#oj*6yu$5d-7@mcw-)a%_@gn-x1@muva_=+wn!pm'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_CONTEXT_PROCESSORS = (
   "django.core.context_processors.auth",
   "django.core.context_processors.debug",
   "django.core.context_processors.i18n",
   "django.core.context_processors.media",
   "django.core.context_processors.request",
   "context_processors.current_site",
   "context_processors.current_page",
   "social_auth.context_processors.social_auth_by_type_backends"
)


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',

    # Third party applications
    'social_auth',
    'easy_thumbnails',
    'south',

    # Internal applications
    'blog',
    'events',
    'profiles',
    'websites',
)

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.facebook.FacebookBackend',
    'social_auth.backends.google.GoogleBackend',
    'django.contrib.auth.backends.ModelBackend',
)

LOGIN_URL = '/login-form/'
LOGIN_REDIRECT_URL = '/'
LOGIN_ERROR_URL = '/login-error/'

SOCIAL_AUTH_ERROR_KEY = 'social_errors'
SOCIAL_AUTH_COMPLETE_URL_NAME = 'complete'
SOCIAL_AUTH_ASSOCIATE_URL_NAME = 'associate_complete'
SOCIAL_AUTH_DEFAULT_USERNAME = 'djangocu'
SOCIAL_AUTH_ENABLED_BACKEND = ('google', 'facebook')

AUTH_PROFILE_MODULE = 'profiles.Profile'
