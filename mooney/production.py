from .base import *
import os
# from decouple import config

print("AMBIENTE PRODUCTION")

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.seuprovedor.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'seu_email@provedor.com'
EMAIL_HOST_PASSWORD = 'sua_senha_de_email'

SECRET_KEY = os.getenv('SECRET_KEY')

ALLOWED_HOSTS = ['seudominio.com']

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
