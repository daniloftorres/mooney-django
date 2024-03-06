#!/bin/bash

# env
cp ./config/local/.env.local ./.env

# Coleta arquivos estáticos
python manage.py collectstatic --noinput

# Inicia o Gunicorn
exec gunicorn --reload mooney.wsgi:application --bind 0.0.0.0:8000