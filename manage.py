#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
# from decouple import Config, RepositoryEnv
# env_path = 'mooney/.env'

# Carrega as variáveis de ambiente do arquivo .env
# config = Config(RepositoryEnv(env_path))

# backend/mooney/mooney/local.py


def main():
    """Run administrative tasks."""

    # Padrão para 'local' se 'ENV' não estiver definido
    # env = config('ENV', default='local')
    # print("manage.py :: ", os.getenv('ENV'))
    # print("checando var env direta :: ", env)
    # print("montando var config :: ", f'mooney.{env}')
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'mooney.local')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
