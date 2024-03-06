10. Language

```python
    # Adicione 'django.middleware.locale.LocaleMiddleware' ao MIDDLEWARE
    MIDDLEWARE = [
        ...
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.locale.LocaleMiddleware',  # Adicione esta linha
        'django.middleware.common.CommonMiddleware',
        ...
    ]

    # Defina os idiomas que seu site suportará
    LANGUAGES = [
        ('en', 'English'),
        ('pt-br', 'Português Brasileiro'),
        # Adicione mais conforme necessário
    ]

    # Caminho para os diretórios onde os arquivos de tradução serão armazenados
    LOCALE_PATHS = [
        BASE_DIR / 'locale/',
    ]

    # Defina o idioma padrão para o site
    LANGUAGE_CODE = 'en-us'

    # Use o fuso horário do usuário
    USE_I18N = True

    # Use datas e números localizados
    USE_L10N = True
```

```Dockerfile
    # Install dependencies including gettext for i18n support
    RUN apt-get update && \
        apt-get install -y gettext && \
        rm -rf /var/lib/apt/lists/* && \
        pip install --no-cache-dir -r config/local/requirements.txt
```

```bash
    python manage.py makemessages -l pt_BR
    python manage.py makemessages -l en_us
```

```bash
    python manage.py compilemessages
```

apps/account/models.py

```python
    LANGUAGE*CHOICES = [
        ('en', *('English')),
        ('pt-br', \_('Portuguese (Brazil)')), # Adicione mais idiomas conforme necessário
    ]
```

apps/account/models.py

```python
    language = models.CharField(max*length=10, choices=LANGUAGE_CHOICES,
    default='en', verbose_name=*('Preferred Language'))
```

```python
    from django.utils import translation
    from django.utils.deprecation import MiddlewareMixin

    apps/account/UserLanguageMiddleware.py
    class UserLanguageMiddleware(MiddlewareMixin):
        def process_request(self, request):
            if request.user.is_authenticated:
                user_language = getattr(request.user, 'language', 'en')
                translation.activate(user_language)
                request.LANGUAGE_CODE = translation.get_language()
```
