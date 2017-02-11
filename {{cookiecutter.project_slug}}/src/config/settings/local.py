from .common import *

DEBUG = True
ALLOWED_HOSTS = []

AUTH_PASSWORD_VALIDATORS = []

CORS_ORIGIN_ALLOW_ALL = True

SECRET_KEY = 'CHANGEME!'

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': '{{cookiecutter.project_slug}}',
        'USER': '{{cookiecutter.project_slug}}',
        'PASSWORD': '{{cookiecutter.project_slug}}',
        'HOST': 'postgres',
        'PORT': '5432',
    }
}
