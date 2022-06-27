from __future__ import absolute_import,unicode_literals
from .base import *
import dj_database_url
import os
env  = os.environ.copy()
SECRET_KEY = env['SECRET_KEY']
DEBUG = True


STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
DATABASES['default'] = dj_database_url.config()
DEFAULT_FILE_STORAGE = env['DEFAULT_FILE_STORAGE']
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO","https")
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': env['CLOUD_NAME'],
    'API_KEY': env['API_KEY'],
    'API_SECRET': env['API_SECRET']
}
STATIC_ROOT = "/app/static/"
ALLOWED_HOSTS =["*"]
try:
    from .local import *
except ImportError:
    pass
