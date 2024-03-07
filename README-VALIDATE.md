# Project Fluxo de Caixa

# Índice

- [Estrutura de Pastas](#estrutura-de-pastas)
- [Pré-requisitos](#pré-requisitos)
- [Instalação e Configuração Docker & Docker Compose](#Instalação-e-configuração-docker--docker-compose)
- [Instalação e Configuração Django](#Instalação-e-configuração-django)

## Estrutura de Pastas e Arquivos

    ```bash
    mooney/
    │
    ├── config/
    |   ├── local/
    |       ├── nginx-config.py
    |       ├── Dockerfile.py
    |       ├── .env
    |       └── requirements.txt
    |
    ├── mooney/
    │   ├── __init__.py
    │   ├── settings/
    │   │   ├── __init__.py
    │   │   ├── base.py
    │   │   ├── development.py
    │   │   ├── production.py
    │   │   └── testing.py
    │   ├── urls.py
    │   ├── asgi.py
    │   └── wsgi.py
    │
    ├── apps/
    │   ├── __init__.py
    │   ├── core/
    │   │   ├── __init__.py
    │   │   ├── admin.py
    │   │   ├── migrations/
    │   │   ├── models.py
    │   │   ├── tests/
    │   │   └── views.py
    │   ├── another_app/
    │   │   ├── __init__.py
    │   │   ├── admin.py
    │   │   ├── migrations/
    │   │   ├── models.py
    │   │   ├── tests/
    │   │   └── views.py
    │   └── ...
    │
    ├── static/
    ├── media/
    ├── templates/
    ├── manage.py
    ├── docker-compose.local.yml
    └── docker-compose.production.yml
    ```

    * requirements.txt
    ```bash
        Django==3.2.5
        python-dotenv
    ```

## Ambiente

- Ubuntu 20.04.3 LTS

## Pré-requisitos

- [python3]
- [Pip]
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Instalação do Python

Se o Python 3 não estiver instalado, você pode instalá-lo usando:

```bash
sudo apt update
sudo apt install python3
```

## Verifique se Pip esta instalado

```bash
pip3 --version
```

## Instalação do Pip para Python

O Pip normalmente é instalado com o Python 3 no Ubuntu, mas se não estiver, você pode instalar usando:

```bash
sudo apt install python3-pip
pip3 --version
```

## Instalação e Configuração Docker & Docker Compose

Instalação do Docker e Docker Compose no Ubuntu 20.04.3 LTS
Aqui está um guia passo a passo para instalar o Docker e o Docker Compose em um sistema Ubuntu 20.04.3 LTS.

### Docker

1.  Atualize o banco de dados de pacotes e instale dependências pré-requisitadas:

```bash
sudo apt update
sudo apt install apt-transport-https ca-certificates curl software-properties-common
```

2.  Adicione a chave GPG oficial do Docker:

```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```

3. Adicione a chave GPG oficial do Docker:

```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```

4. Adicione o repositório estável do Docker:

```bash
echo "deb [signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

5. Atualize o banco de dados de pacotes novamente e instale o Docker Engine:

```bash
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io
```

6. Adicione seu usuário ao grupo docker para executar comandos Docker sem precisar de sudo:

```bash
sudo usermod -aG docker $USER
Nota: É necessário fazer logout e login novamente ou reiniciar o sistema para aplicar as alterações.
```

7. Verifique se o Docker está instalado corretamente:

```bash
docker --version
```

### Docker Compose

8. Baixe a versão mais recente do Docker Compose:

```bash
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```

9. Dê permissão de execução ao Docker Compose:

```bash
sudo chmod +x /usr/local/bin/docker-compose
```

10. Verifique se o Docker Compose está instalado corretamente:

```bash
docker-compose --version
```

Agora, você deve ter o Docker e o Docker Compose instalados em seu sistema Ubuntu 20.04.3 LTS. Certifique-se de seguir todos os passos corretamente e verificar as versões para garantir uma instalação bem-sucedida.

## Instalação e Configuração Django

1. Instalação no ambiente local usando o PIP:

```bash
pip install Django==3.2.5
```

2. Iniciando o Projeto Localmente

```bash
django-admin startproject mooney .
```

3. Preparando o Django para Entender Varios Ambientes

   - Altere o arquivo mooney/manage.py :

     ```bash
         import os
         import sys

         if __name__ == '__main__':
             env = os.getenv('ENV', 'local')  # Padrão para 'local' se 'ENV' não estiver definido
             os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'mooney.settings.{env}')

             from django.core.management import execute_from_command_line
             execute_from_command_line(sys.argv)
     ```

   - Altere o arquivo mooney/mooney/wsgi.py :

     ```bash
         import os
         from django.core.wsgi import get_wsgi_application

         env = os.getenv('ENV', 'local')  # Padrão para 'local' se 'ENV' não estiver definido
         os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'mooney.settings.{env}')

         application = get_wsgi_application()
     ```

   - Crie o seguinte arquivo `mooney/mooney/base.py` :

     ```bash
         Copie todo o conteudo do settings.py para ele.
     ```

   - Crie o seguinte aquivo mooney/mooney/local.py :

     ```bash
         from .base import *
     ```

   - Crie o seguinte mooney/mooney/production.py :
     ```bash
         from .base import *
     ```

4. Configuração do Ambiente Local

   - **Docker Compose**

     - Configuração e criação do arquivo `mooney/docker-compose.local.yml` para uso local

       ```bash
           version: '3'

           services:
           db:
               image: postgres
               env_file:
               - .env
               volumes:
               - postgres_data:/var/lib/postgresql/data/
           web:
               image: web
               command: gunicorn docker_django.wsgi:application --bind 0.0.0.0:8000
               ports:
               - 8000:8000
               depends_on:
               - db
               environment:
               - SQL_ENGINE=django.db.backends.postgresql
               - SQL_DATABASE=postgres
               - SQL_USER=postgres
               - SQL_PASSWORD=postgres
               - SQL_HOST=db
               - SQL_PORT=5432
           nginx:
               image: nginx
               ports:
               - 80:80
               volumes:
               - ./nginx:/etc/nginx/conf.d
               depends_on:
               - web

           volumes:
           postgres_data:

       ```

   - **Env**

     - Configuração e criação do `mooney/config/local/.env` para uso local

     ```bash
         POSTGRES_DB=seu_banco_de_dados
         POSTGRES_USER=seu_usuario
         POSTGRES_PASSWORD=sua_senha
     ```

     Copiar o arquivo mooney/config/local/.env para a raiz do projeto mooney/.env

   - **Nginx**

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

             include /etc/nginx/conf.d/*.conf;
         }
     ```

   - **Nginx**

     - Configuração e criação do `mooney/config/local/nginx/conf.d/mooney.conf` para uso local

     ```bash
         # Configurações específicas do mooney
         server {
             listen 80;
             server_name mooney.com;

             location / {
                 proxy_pass http://django:8000;
                 proxy_set_header Host $host;
                 proxy_set_header X-Real-IP $remote_addr;
                 proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
             }
         }
     ```

5. Configuração do Ambiente Produção
   **sera criado por ultimo\***

6. Configuração Banco de Dados
   Nos arquivos de configuração:
   `mooney/mooney/base.py`

   Configure as variáveis de ambiente da seguinte forma:

   ```bash
       import os

       DATABASES = {
           'default': {
               'ENGINE': os.getenv('DB_ENGINE', 'django.db.backends.sqlite3'),
               'NAME': os.getenv('db_table', os.path.join(BASE_DIR, 'db.sqlite3')),
               'USER': os.getenv('DB_USER', ''),
               'PASSWORD': os.getenv('DB_PASSWORD', ''),
               'HOST': os.getenv('DB_HOST', 'localhost'),
               'PORT': os.getenv('DB_PORT', ''),
           }
       }
   ```

7. Migrações Iniciais

```bash
python manage.py migrate
```

3. Arquivos Estaticos

   - Estrutura de Diretórios

     - Criar as pastas no mesmo lugar onde esta o manage.py \*\*
       ├── static/

     - No seu arquivo settings.py, defina as seguintes configurações:

     ```bash
         import os
         BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

         STATIC_URL = '/static/'
         STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]
         STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
     ```

     ```bash
         STATIC_URL = '/static/'
         STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
     ```

   - Coletando Arquivos Estáticos

     - Em produção, você precisa coletar todos os arquivos estáticos das aplicações e colocá-los em STATIC_ROOT. Use o comando:

     ```bash
         python manage.py collectstatic
     ```

   - Em desenvolvimento
     Durante o desenvolvimento, o Django pode servir arquivos estáticos para você. Isso é feito automaticamente se você estiver usando django.contrib.staticfiles e DEBUG estiver definido como True no seu settings.py.

   - Em produção
     Em produção, o Django não serve arquivos estáticos. Você precisa configurar seu servidor web (como Nginx ou Apache) para servir os arquivos estáticos.

     Configuração do Nginx para Arquivos Estáticos
     No Nginx, você configuraria um bloco de localização para servir arquivos estáticos. Por exemplo:

     ```bash
         server {
             ...

             location /static/ {
                 alias /path/to/your/staticfiles/;
             }
         }
     ```

```bash
python manage.py migrate
```

###### criado ate aqui

1. Clone o repositório do Django:

```bash
git clone https://github.com/django/django.git
cd django
```

2. Crie um arquivo .env na raiz do projeto e adicione as configurações do Django.

```bash
touch .env
```

3. Adicione o seguinte conteúdo ao .env:

```bash
DJANGO_SECRET_KEY=seu_secret_key_aqui
DJANGO_DEBUG=True
```

Substitua seu_secret_key_aqui pela chave secreta do Django de sua escolha. Para gerar uma chave secreta, você pode usar Django Secret Key Generator.

4. Configure o ambiente de desenvolvimento com Docker Compose.

```bash
docker-compose up
```

Este comando iniciará o PostgreSQL, o servidor Django e permitirá o acesso à aplicação em http://localhost:8000/.

5. Para criar as migrações do banco de dados e aplicá-las, abra um novo terminal e execute:

```bash
docker-compose exec web python manage.py migrate
```

6. Se você precisar criar um superusuário, execute o seguinte comando:

```bash
docker-compose exec web python manage.py createsuperuser
```

- Entidade Login

  - Jwt
  - OAuth
  - OAuth 2.0 e JWT
  - Autenticação de Dois Fatores (2FA

- Entidade Cliente - Cadastro - Edição - Remoção

- Entidade Produto

  - Cadastro
  - Edição
  - Remoção

  -Categoria de Produto

- Venda

  - Cadastro
  - Edição
  - Remoção

  - Forma de Pagamento
  - Venda Parcela

```bash
python manage.py migrate
```
