"""
WSGI config for mooney project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from decouple import Config, RepositoryEnv
# env_path = 'mooney/.env'

# Carrega as variáveis de ambiente do arquivo .env
# config = Config(RepositoryEnv(env_path))

# env = config('ENV', 'local')  # Padrão para 'local' se 'ENV' não estiver definido
# env = config('ENV', default='local')
# print("wsgi.py usando getenv:: ", os.getenv('ENV'))
# print("wsgi.py usando config:: ", config('ENV'))
# print("checando var env direta :: ", env)
# print("montando var config :: ", f'mooney.{env}')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'mooney.local')

application = get_wsgi_application()
