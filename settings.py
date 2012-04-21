# -*- coding: utf-8 -*-
from os import path
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS

DEBUG = False
TEMPLATE_DEBUG = DEBUG
ROOT = path.realpath(path.dirname(__file__))

ADMINS = (
    (u'Onur Mat', 'omat@teknolab.org'),
    (u'Gökmen Görgen', 'gokmen@alageek.com')
)
MANAGERS = ADMINS
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'sqlite.db'
    }
}
MEDIA_URL = '/media/'
MEDIA_ROOT = path.join(ROOT, '.media')
TIME_ZONE = 'Europe/Istanbul'
LANGUAGE_CODE = 'tr'
SITE_ID = 1
DEFAULT_FROM_EMAIL = 'Django <django@django.org.tr>'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_SUBJECT_PREFIX = '[django-tr] '
STATIC_URL = '/static/'
STATIC_ROOT = path.join(ROOT, '.static')
STATICFILES_DIRS = (path.join(ROOT, 'static'),)
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
TEMPLATE_CONTEXT_PROCESSORS += (
   "django.core.context_processors.request",
   "context_processors.current_site",
   "context_processors.current_page",
   "social_auth.context_processors.social_auth_by_type_backends"
)
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'django.contrib.admin',

    # Third party applications
    'social_auth',
    'tumblr_auth',
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
    'social_auth.backends.twitter.TwitterBackend',
    'tumblr_auth.backend.TumblrBackend',
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
SOCIAL_AUTH_ENABLED_BACKENDS = ('google', 'facebook', 'tumblr', 'twitter')
AUTH_PROFILE_MODULE = 'profiles.Profile'
SOCIAL_AUTH_IMPORT_BACKENDS = ('tumblr_auth',)

## Local Settings
try:
    from local_settings import *
except ImportError:
    pass
