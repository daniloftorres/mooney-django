4. Timezone

   - `apps/account/TimezoneMiddleware.py`

     ```python
         from django.utils import timezone


         class TimezoneMiddleware:
             def __init__(self, get_response):
                 self.get_response = get_response

             def __call__(self, request):
                 if request.user.is_authenticated:
                     # Supondo que o modelo de perfil do usuário tenha um campo 'timezone'
                     tz_str = request.user.profile.timezone
                     if tz_str:
                         timezone.activate(tz_str)
                     else:
                         timezone.deactivate()
                 response = self.get_response(request)
                 return response

     ```

   - `mooney/base.py`

   ```python
       MIDDLEWARE = [
           ...
           'django.contrib.sessions.middleware.SessionMiddleware',
           'django.middleware.locale.LocaleMiddleware',
           'django.contrib.auth.middleware.AuthenticationMiddleware',
           'django.contrib.messages.middleware.MessageMiddleware',
           'django.middleware.common.CommonMiddleware',
           'django.middleware.security.SecurityMiddleware',
           'django.middleware.clickjacking.XFrameOptionsMiddleware',
           'django.middleware.timezone.TimezoneMiddleware',
       ]

       USE_TZ = True
   ```

- `config/local/requirements.txt`

  - Biblioteca com listagem de timezone
    ```txt
        pytz
    ```

- `apps/account/models.py`

  - Exemplo de uso onde o usuario pode escolher a timezone

  ```python
      import pytz

      timezone = models.CharField(max_length=50, choices=[(
              tz, tz) for tz in pytz.all_timezones], default='UTC', verbose_name=_('Preferred Timezone'))
  ```

- `apps/account/admin.py` - Biblioteca com listagem de timezone

  ```python
    list_display = UserAdmin.list_display + ('timezone',)

    # Adicione o campo de timezone ao fieldset para permitir a edição no formulário do usuário
    fieldsets = UserAdmin.fieldsets + (
        (_('Personal info'), {
         'fields': ('age', 'timezone', 'full_name', 'language')}),
    )

    # Se você quiser permitir a edição de timezone ao criar um novo usuário, atualize esta configuração também
    add_fieldsets = UserAdmin.add_fieldsets + (
        (_('Personal info'), {
         'fields': ('age', 'timezone', 'full_name', 'language')}),
  ```
