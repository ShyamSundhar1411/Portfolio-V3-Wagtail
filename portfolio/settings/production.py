from __future__ import absolute_import,unicode_literals
from .base import *
import environ
import dj_database_url
import os

env = environ.Env()
environ.Env.read_env()
SECRET_KEY = env.str('SECRET_KEY')
DEBUG = False
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
DATABASES['default'] =  dj_database_url.config()
DEFAULT_FILE_STORAGE = env.str('DEFAULT_FILE_STORAGE')
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO","https")
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_USE_TLS = True
EMAIL_USER_SSL = False
EMAIL_HOST = env.str('EMAIL_HOST',default = '')
EMAIL_HOST_USER = env.str('EMAIL_HOST_USER',default = '')
EMAIL_HOST_PASSWORD = env.str('EMAIL_HOST_PASSWORD',default = '')
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = "Notification Bot<noreply@shyamsundhar.com>"
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': env.str('CLOUD_NAME'),
    'API_KEY': env.str('API_KEY'),
    'API_SECRET': env.str('API_SECRET'),
    'API_PROXY': 'http://proxy.server:3128'
}
ALLOWED_HOSTS =["*"]
try:
    from .local import *
except ImportError:
    pass
