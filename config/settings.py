from assessment.settings.base import *
from pathlib import Path

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'assessment',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST':'localhost'
    }
}
