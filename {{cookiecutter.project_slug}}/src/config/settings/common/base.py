import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'
