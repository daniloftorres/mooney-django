# Usuário

- [Settings](#docs/django/usuario/settings.md)
- [Model](#docs/django/usuario/model.md)
- [Admin](#docs/django/usuario/admin.md)
- [API RESTFULL](#docs/django/usuario/api-restfull.md)
- [Autenticação](#docs/django/usuario/autenticacao.md)

## Criando o app account

## Settings

Configurando o django para usar um model customizado.

1. `mooney/mooney/base.py`

   ```bash
       DEFAULT_HOST = 'admin-django'

       INSTALLED_APPS = [
           'django.contrib.admin',
           'django.contrib.auth',
           'django.contrib.contenttypes',
           'django.contrib.sessions',
           'django.contrib.messages',
           'django.contrib.staticfiles',
           'django_hosts',


           'apps.account',
       ]
   ```

## Model

## Admin

## Autenticação JWT

1. `mooney/mooney/base.py`

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
           'rest_framework_simplejwt',
       ]

       MIDDLEWARE = [
           'django_hosts.middleware.HostsRequestMiddleware',
           'django.middleware.security.SecurityMiddleware',
           'django.contrib.sessions.middleware.SessionMiddleware',
           'django.middleware.common.CommonMiddleware',
           'django.middleware.csrf.CsrfViewMiddleware',
           'django.contrib.auth.middleware.AuthenticationMiddleware',
           'django.contrib.messages.middleware.MessageMiddleware',
           'django.middleware.clickjacking.XFrameOptionsMiddleware',
           'django_hosts.middleware.HostsResponseMiddleware',
       ]

       REST_FRAMEWORK = {
           'DEFAULT_AUTHENTICATION_CLASSES': (
               'rest_framework_simplejwt.authentication.JWTAuthentication',
           ),
       }
   ```

2. `mooney/mooney/routes/urls_api.py`

   ```bash
       from django.urls import path, include
       from rest_framework import routers
       from rest_framework_simplejwt.views import (
           TokenObtainPairView,
           TokenRefreshView,
       )

       urlpatterns = [
           path('v1/token/', TokenObtainPairView.as_view(), name="token_obtain_pair"),
           path('v1/token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
       ]
   ```

3. `mooney/apps/customer/api/v1/tests.py`

   ```bash
       # customer/api/v1/tests.py
       import requests
       from django.urls import reverse
       from rest_framework import status
       from rest_framework.test import APITestCase
       from rest_framework_simplejwt.tokens import RefreshToken
       from django.contrib.auth.models import User


       class JWTAuthTest(APITestCase):
           def setUp(self):
               # Cria um usuário para testar a autenticação
               self.user = User.objects.create_user(
                   username='testuser2', password='testpassword2')
               self.token = RefreshToken.for_user(
                   self.user)  # Gera token para o usuário

           def test_jwt_auth(self):
               # Define o token no cabeçalho de autorização
               self.client.credentials(
                   HTTP_AUTHORIZATION=f'Bearer {self.token.access_token}')
               url = reverse('customer-list')
               response = self.client.get(url, follow=True)
               print("response.status_code :: ", response.status_code)
               self.assertEqual(response.status_code, status.HTTP_200_OK)

   ```

   Comando para executar teste unitario

   ```bash
       python manage.py test apps.customer.api.v1.tests
       python manage.py test apps.erp.transaction.api.v1.tests
   ```

   Comando para executar teste todos unitario

   ```bash
       python manage.py test apps
   ```

## Autenticação OAuth

1. `mooney/mooney/base.py`

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
            'oauth2_provider',

            'apps.account',
        ]

       REST_FRAMEWORK = {
            'DEFAULT_AUTHENTICATION_CLASSES': (
                'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
            ),
        }
   ```

2. `mooney/mooney/routes/urls_api.py`

   ```bash
       from django.urls import path, include
       from rest_framework import routers
       from rest_framework_simplejwt.views import (
           TokenObtainPairView,
           TokenRefreshView,
       )

       urlpatterns = [
           path('v1/oauth2/', include('oauth2_provider.urls', namespace='oauth2_provider')),
       ]
   ```

3. Comando migrate criar app oauth2

   ```bash
       python manage.py migrate
   ```

4. Configuração do cliente oauth2

   - Navegue até o django-oauth-toolkit na seção de aplicações e clique em "Add".
   - Preencha os detalhes necessários para a sua aplicação OAuth.
     - O campo "Client type" deve ser ajustado com base no seu fluxo OAuth (ex.: "Confidential" para fluxos que podem armazenar segredos de forma segura, como aplicações web).
     - O campo "Authorization grant type" determina o tipo de fluxo OAuth (ex.: "Authorization code" para fluxos com código de autorização).
   - Após configurar e salvar sua aplicação, você receberá um client_id e client_secret que serão usados para autenticar sua aplicação cliente.

   ```bash
       cliente id : 2LxBKN35djDbHhgvkMR7npMWWi0gKmtdlFyzVHQw
       cliente secret : 4FzCjVqfzipitUNMi3hZByGeRUDhDRkwCK9wVbJPN4CME8AxzGnh7KT6Gh6uMOBiCLexZ5EyBeLmPS1IVevpAlJjeionAUqRbZQQN9cG6NjTEtPdnNFDcnPw4znoPfK5
   ```

   curl code first step

   ```bash
        curl --location 'http://api.mooney.com/v1/oauth2/token/' \
        --form 'grant_type="client_credentials"' \
        --form 'client_id="2LxBKN35djDbHhgvkMR7npMWWi0gKmtdlFyzVHQw"' \
        --form 'client_secret="4FzCjVqfzipitUNMi3hZByGeRUDhDRkwCK9wVbJPN4CME8AxzGnh7KT6Gh6uMOBiCLexZ5EyBeLmPS1IVevpAlJjeionAUqRbZQQN9cG6NjTEtPdnNFDcnPw4znoPfK5"'
   ```

curl code second step

```bash
     curl --location 'http://api.mooney.com/v1/oauth2/token/' \
     --form 'grant_type="client_credentials"' \
     --form 'client_id="2LxBKN35djDbHhgvkMR7npMWWi0gKmtdlFyzVHQw"' \
     --form 'client_secret="4FzCjVqfzipitUNMi3hZByGeRUDhDRkwCK9wVbJPN4CME8AxzGnh7KT6Gh6uMOBiCLexZ5EyBeLmPS1IVevpAlJjeionAUqRbZQQN9cG6NjTEtPdnNFDcnPw4znoPfK5"'
```

    Configuração client credentials
       ```bash
       name : oauth2-mooney-client-credentials
       Client type: confidential
       Authorization Grant Type : Client credentials
       cliente id : 76rpCwJqi34TCtR5euRlixQWBFfmt0zXYLvmYWDr
       cliente secret : z63fKkzs9e3Ux22KlhnGvQNSYz1IIjdGr5OgIW228ZAmmebJckKyJPOzix4PfygE1VYrvf68KrT5BgqPyhPWolytvrcrSzXomXqgHA8u6xhILjwdqVHirPdMqVQESUCT

```

```
