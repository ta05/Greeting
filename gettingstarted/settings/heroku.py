"""
Production Settings for Heroku
"""

import environ
import dj_database_url 


# If using in your own project, update the project namespace below
from gettingstarted.settings.base import *

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# False if not in os.environ
DEBUG = True

# Raises django's ImproperlyConfigured exception if SECRET_KEY not in os.environ
SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

DATABASE_URL = env('DATABASE_URL')
# Parse database connection url strings like psql://user:pass@127.0.0.1:8458/db
DATABASES['default'] = dj_database_url.parse(DATABASE_URL, conn_max_age=500)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}