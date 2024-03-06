# Estrutura de Pastas e Arquivos

    ```bash
      ├── mooney/
      │   ├── apps/
      │   │   ├── core/
      │   │   │   ├── api/
      │   │   │   │   ├── v1/
      │   │   │   │   │   └── admin.py
      │   │   │   │   │   └── apps.py
      │   │   │   │   │   └── __init__.py
      │   │   │   │   │   ├── migrations/
      │   │   │   │   │   │   └── __init__.py
      │   │   │   │   │   └── tests.py
      │   │   │   │   │   └── views.py
      │   │   │   └── apps.py
      │   │   │   └── __init__.py
      │   │   │   ├── migrations/
      │   │   │   │   └── __init__.py
      │   │   │   └── models.py
      │   │   ├── customer/
      │   │   │   └── admin.py
      │   │   │   ├── api/
      │   │   │   │   ├── v1/
      │   │   │   │   │   └── admin.py
      │   │   │   │   │   └── __init__.py
      │   │   │   │   │   └── serializers.py
      │   │   │   │   │   └── tests.py
      │   │   │   │   │   └── views.py
      │   │   │   └── apps.py
      │   │   │   └── __init__.py
      │   │   │   ├── migrations/
      │   │   │   │   └── 0001_initial.py
      │   │   │   │   └── __init__.py
      │   │   │   └── models.py
      │   ├── config/
      │   │   ├── local/
      │   │   │   └── Dockerfile
      │   │   │   └── entrypoint.sh
      │   │   │   ├── nginx/
      │   │   │   │   ├── conf.d/
      │   │   │   │   │   └── mooney.conf
      │   │   │   │   └── nginx_antigo.conf
      │   │   │   │   └── nginx.conf
      │   │   │   ├── postgres/
      │   │   │   │   └── postgresql.conf
      │   │   │   └── requirements.txt
      │   │   ├── postgres/
      │   │   │   ├── postgresql.conf/
      │   │   │   │   └── *
      │   │   ├── production/
      │   │   │   └── *
      │   │   ├── staging/
      │   │   │   └── *
      │   └── docker-compose.local copy.yml
      │   └── docker-compose.local.yml
      │   └── docker-compose.production.yml
      │   └── draw_tree.sh
      │   └── manage.py
      │   ├── mooney/
      │   │   └── asgi.py
      │   │   └── base.py
      │   │   └── __init__.py
      │   │   └── local.py
      │   │   ├── media/
      │   │   │   └── *
      │   │   └── production.py
      │   │   ├── routes/
      │   │   │   └── admin.py
      │   │   │   ├── api/
      │   │   │   │   ├── v1/
      │   │   │   │   │   └── account.py
      │   │   │   │   │   └── urls.py
      │   │   │   └── hosts.py
      │   │   │   └── urls_api.py
      │   │   │   ├── urls_old/
      │   │   │   │   └── admin.py
      │   │   │   │   └── api.py
      │   │   │   └── urls.py
      │   │   └── settings.py
      │   │   └── urls.py
      │   │   └── wsgi.py
      │   └── my-pg_hba.conf
      │   └── my-postgresql.conf
      │   └── README.md
      │   └── README-VALIDATE.md
      │   └── structure.txt

    ```
