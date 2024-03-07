4. Configuração Banco de Dados
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

5. Migrações Iniciais

   ```bash
   python manage.py migrate
   ```
