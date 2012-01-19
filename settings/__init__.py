# -*- coding: utf-8 -*-
from os import path
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS

MEDIA_URL = '/media/'
TIME_ZONE = 'Europe/Istanbul'
LANGUAGE_CODE = 'tr'
SITE_ID = 1
DEFAULT_FROM_EMAIL = 'Django <django@django.org.tr>'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_SUBJECT_PREFIX = '[django-tr] '
STATIC_URL = '/static/'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
USE_I18N = False
USE_L10N = False
ADMIN_MEDIA_PREFIX = '/static/admin/'
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)
ROOT_URLCONF = 'urls'
TEMPLATE_CONTEXT_PROCESSORS = TEMPLATE_CONTEXT_PROCESSORS + (
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
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'django.contrib.admin',

    # Third party applications
    'social_auth',
    'easy_thumbnails',
    'south',

    # Internal applications
    'apps.core',
    'apps.events',
    'apps.planet',
    'apps.profiles',
    'apps.websites',
)
AUTHENTICATION_BACKENDS = (
    'social_auth.backends.facebook.FacebookBackend',
    'social_auth.backends.google.GoogleBackend',
    'django.contrib.auth.backends.ModelBackend',
)

## Social Auth Settings
LOGIN_URL = '/login-form/'
LOGIN_REDIRECT_URL = '/'
LOGIN_ERROR_URL = '/login-error/'
SOCIAL_AUTH_ERROR_KEY = 'social_errors'
SOCIAL_AUTH_COMPLETE_URL_NAME = 'socialauth_complete'
SOCIAL_AUTH_ASSOCIATE_URL_NAME = 'socialauth_associate_complete'
SOCIAL_AUTH_DEFAULT_USERNAME = 'djangocu'
SOCIAL_AUTH_ENABLED_BACKENDS = ('google', 'facebook')
AUTH_PROFILE_MODULE = 'profiles.Profile'

# Pubsubhubbub settings
PUSH_HUB = 'https://superfeedr.com/hubbub'
PUSH_CREDENTIALS = 'apps.aggregator.utils.push_credentials'
PUSH_SSL_CALLBACK = True

## Local Settings
from settings.default import *
try:
    from bundle_config import config

    DEBUG = False
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': config['postgres']['database'],
            'USER': config['postgres']['username'],
            'PORT': int(config['postgres']['port']),
            'HOST': config['postgres']['host'],
            'PASSWORD': config['postgres']['password']
        }
    }

except ImportError:
    pass

# FIXME: use settings_local.py, it's dirty solution.
try:
    from settings.local import *
except ImportError:
    pass
