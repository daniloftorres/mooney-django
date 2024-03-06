# Ambientes

# Índice

- [Local](#local)
- [Produção](#producao)

## Local

1. Docker Compose

   - Configuração e criação do arquivo `mooney/docker-compose.local.yml` para uso local

   ```bash
       version: '3'

       services:
           django:
           build:
               context: .
               dockerfile: ./config/local/Dockerfile
           ports:
               - "8000:8000"
           depends_on:
               - postgres
           env_file:
               - ./config/local/.env.local
           volumes:
               - .:/app

           postgres:
           image: postgres:14.1-alpine
           volumes:
               - ./postgres-data:/var/lib/postgresql/data
               - ./my-postgresql.conf:/etc/postgresql/postgresql.conf
               - ./my-pg_hba.conf:/etc/postgresql/pg_hba.conf
           restart: always
           env_file:
               - ./config/local/.env.local
           ports:
               - "5432:5432"


           nginx:
           image: nginx:latest
           ports:
               - "80:80"
           volumes:
               - ./mooney/static/:/app/mooney/static/
               - ./config/local/nginx/nginx.conf:/etc/nginx/nginx.conf
               - ./config/local/nginx/conf.d:/etc/nginx/conf.
           depends_on:
               - django

       volumes:
           postgres_data:
           static:

   ```

2. Env

   - Configuração e criação do `mooney/config/local/.env` para uso local

   ```bash
       ENV=local
       DEBUG=1
       SECRET_KEY=3bbnu(arlk^jwn8c56-&wsk-%n-wm469ass)bcbav5@=5llg3&
       DB_ENGINE=django.db.backends.postgresql
       POSTGRES_DB=mooney_db
       POSTGRES_USER=mooney_user
       POSTGRES_PASSWORD=mooney_password
       DB_PASSWORD=mooney_password
       DB_HOST=postgres
       DB_PORT=5432
       PGDATA=./tmp/db
   ```

   Copiar o arquivo mooney/config/local/.env para a raiz do projeto mooney/.env

3. Nginx

   - Configuração e criação do `mooney/config/local/nginx/nginx.conf` para uso local

   ```bash
       user nginx;
       worker_processes auto;

       error_log /var/log/nginx/error.log;
       pid /var/run/nginx.pid;

       events {
           worker_connections 1024;
       }

       http {
           include /etc/nginx/mime.types;
           default_type application/octet-stream;

           log_format main '$remote_addr - $remote_user [$time_local] "$request" '
                               '$status $body_bytes_sent "$http_referer" '
                               '"$http_user_agent" "$http_x_forwarded_for"';

           access_log /var/log/nginx/access.log main;

           sendfile on;
           tcp_nopush on;
           tcp_nodelay on;
           keepalive_timeout 65;
           types_hash_max_size 2048;

           #include /etc/nginx/conf.d/*.conf;

           server {
               listen 80;
               server_name admin.mooney.com;

               location / {
                       proxy_pass http://django:8000;
                       proxy_set_header Host $host;
                       proxy_set_header X-Real-IP $remote_addr;
                       proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                   }

               location /static/ {
                   alias /app/mooney/static/;
               }
           }

           server {
               listen 80;
               server_name api.mooney.com;

               location / {
                   proxy_pass http://django:8000/api;
                   proxy_set_header Host $host;
                   proxy_set_header X-Real-IP $remote_addr;
                   proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
               }
           }

       }

   ```

## Produção
