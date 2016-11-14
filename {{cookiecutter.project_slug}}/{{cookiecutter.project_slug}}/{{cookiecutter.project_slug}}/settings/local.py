from .common import *

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
