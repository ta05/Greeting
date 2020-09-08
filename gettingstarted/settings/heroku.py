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
DEBUG = env('DEBUG')

# Raises django's ImproperlyConfigured exception if SECRET_KEY not in os.environ
SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

DATABASE_URL = env('DATABASE_URL')
# Parse database connection url strings like psql://user:pass@127.0.0.1:8458/db
DATABASES['default'] = dj_database_url.parse('postgres://jsefvoapkecivr:4009246d6062f477a9c09a3f16e578d4f01968dd0f367613ece3829ea893e52b@ec2-52-202-66-191.compute-1.amazonaws.com:5432/d7m28n3sitso46', conn_max_age=500)