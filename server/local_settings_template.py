import settings
import os

# ======================================
# Mandatory settings
# ======================================

# Key used by Django for Cryptographic signing
SECRET_KEY = 'CHANGE_THIS_STRING'

# TEST Keys used for Stripe processing


MEMCACHEIFY_USE_LOCAL=True


DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.postgresql_psycopg2', 
        'NAME': '[db_name]',
        'USER': '[db_user]',
        'PASSWORD': '[password]',
        'HOST': '[your host]'
    }
}

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

EMAIL_HOST = 'localhost'
EMAIL_HOST_USER = 'USERNAME'
EMAIL_HOST_PASSWORD = 'MY_PASSWORD'
EMAIL_PORT = 25
EMAIL_USE_TLS = False
EMAIL_USE_SSL = False
DEFAULT_FROM_EMAIL = "no-reply@zober.com"

DEBUG = True
# TEMPLATE_DEBUG = True

