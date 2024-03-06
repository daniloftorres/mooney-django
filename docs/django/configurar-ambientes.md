3. Preparando o Django para Entender Varios Ambientes

   - Altere o arquivo mooney/manage.py :

     ```bash
         import os
         import sys

         if __name__ == '__main__':
             env = os.getenv('ENV', 'local')
             os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'mooney.settings.{env}')

             from django.core.management import execute_from_command_line
             execute_from_command_line(sys.argv)
     ```

   - Altere o arquivo mooney/mooney/wsgi.py :

     ```bash
         import os
         from django.core.wsgi import get_wsgi_application

         env = os.getenv('ENV', 'local')
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
