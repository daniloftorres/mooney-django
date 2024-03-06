5. Arquivos Estaticos

- **Descrição**

  - Em desenvolvimento
    Durante o desenvolvimento, o Django pode servir arquivos estáticos para você. Isso é feito automaticamente se você estiver usando django.contrib.staticfiles e DEBUG estiver definido como True no seu settings.py.

  - Em produção
    Em produção, o Django não serve arquivos estáticos. Você precisa configurar seu servidor web (como Nginx ou Apache) para servir os arquivos estáticos.

- As pastas serão configuradas para serem criadas :

  - mooney/mooney/static

- Configurações do (settings.py) no nosso caso é o `mooney/mooney/local.py`

  ```bash
  STATIC_URL = '/static/'
  STATIC_ROOT = os.path.join(BASE_DIR, 'mooney/static')

  MEDIA_URL = '/media/'
  MEDIA_ROOT = os.path.join(BASE_DIR, 'mooney/media')
  ```

- Configuração do arquivo `docker-compose.local.yml`

  ```bash
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
  ```

- Coletando Arquivos Estáticos acontece no `mooney/config/local/entrypoint.sh`

  - você precisa coletar todos os arquivos estáticos das aplicações e colocá-los em STATIC_ROOT. Use o comando:

    ```bash
        python manage.py collectstatic
    ```

- Configuração do arquivo `mooney/config/local/nginx/nginx.conf`

  ```bash
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
  ```
