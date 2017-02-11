# staticfiles.py
import os

from config.settings.common.base import BASE_DIR

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, '../static'),
)
