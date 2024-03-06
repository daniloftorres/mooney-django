from .base import *
import os

print("AMBIENTE LOCAL")

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.seuprovedor.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'seu_email@provedor.com'
EMAIL_HOST_PASSWORD = 'sua_senha_de_email'

# SECRET_KEY = os.getenv('SECRET_KEY')
# SECRET_KEY = "django-insecure-*gq8)xj3ufyb#myla^9isdr4p44oe5pgb7t)%7i(i&&3@42q(e"

ALLOWED_HOSTS = ['*']

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'mooney/static')
print("STATIC_ROOT", STATIC_ROOT)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'mooney/media')
print("MEDIA_ROOT", MEDIA_ROOT)

SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

# os.getenv('ENV', 'local')
