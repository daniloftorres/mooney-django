4. Configuração e Instalação dos Hosts (dominios e subdominios).

   - **Descrição**
     Cenário a ser configurado é :
     admin.mooney.com : acesso ao admin django
     api.mooney.com : acesso à coleção de apis do sistema

   - `mooney/config/local/requirements.txt`
     django-hosts==6.0

   - `mooney/mooney/base.py`

     ```bash
       DEFAULT_HOST = 'admin-django'
     ```

     ```bash
       INSTALLED_APPS = [
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
       'django_hosts',
       'rest_framework',

       'apps.core',
       'apps.customer',
       ]
     ```

     ```bash
       MIDDLEWARE = [
       'django_hosts.middleware.HostsRequestMiddleware', # Adicione isso no início
       'django.middleware.security.SecurityMiddleware',
       'django.contrib.sessions.middleware.SessionMiddleware',
       'django.middleware.common.CommonMiddleware',
       'django.middleware.csrf.CsrfViewMiddleware',
       'django.contrib.auth.middleware.AuthenticationMiddleware',
       'django.contrib.messages.middleware.MessageMiddleware',
       'django.middleware.clickjacking.XFrameOptionsMiddleware',
       'django_hosts.middleware.HostsResponseMiddleware', # Adicione isso no final
       ]
     ```

     ```bash
       ROOT_URLCONF = 'mooney.routes.urls_api'
       ROOT_URLADMIN = 'mooney.routes.admin'
       ROOT_HOSTCONF = 'mooney.routes.hosts'
     ```

   - Configuraçõa do arquivo `mooney/mooney/routes/hosts.py`

     ```bash
       from django_hosts import patterns, host

       host_patterns = patterns(
           '',
           host(r'admin', 'mooney.routes.admin', name='admin-django'),
           host(r'api', 'mooney.routes.urls_api', name='api'),
       )
     ```

   - Configuraçõa do arquivo `mooney/mooney/routes/admin.py`

     ```bash
       from django.contrib import admin
       from django.urls import path

       urlpatterns = [
           path('', admin.site.urls),
       ]
     ```

   - Configuraçõa do arquivo `mooney/mooney/routes/urls_api.py`

     ```bash
       from django.urls import path, include
       from rest_framework import routers
       from apps.customer.api.v1.views import CustomerViewSet

       router = routers.DefaultRouter()
       router.register(r'customer', CustomerViewSet)

       urlpatterns = [
           path('v1/', include(router.urls)),
       ]
     ```

   - Configuraçõa do arquivo `mooney/config/local/nginx/nginx.conf`

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
