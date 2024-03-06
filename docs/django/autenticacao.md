# Autenticação

1.  Pré-requisitos gerais

        - Principais suporte do modulo é :

        - Usado para criação de APIs no Django, oferecendo um conjunto abrangente de funcionalidades para esse fim.
        - Serialização, deserialização, tratamento de requisições e respostas, e autenticação, entre outras funcionalidades.
        - Autenticação baseada em sessão, autenticação e pode ser extendido para suportar quase qualquer tipo de autenticação

        ```bash
            pip install django djangorestframework
        ```

# JWT

1.  Pré-requisitos (`backend/mooney/config/local/requirements.txt`)

        - Principais suporte do modulo é :
            - Extensão que adiciona autenticação JWT ao Django Rest Framework, fornecendo uma solução específica para gerenciamento de tokens JWT.
            - Plugin adicional para o Django Rest Framework.
            - Suporte para JSON Web Tokens (JWT) autenticação para DRF

        ```bash
            pip install djangorestframework-simplejwt
        ```

2.  Configurando o settings.py (base.py)

    ```bash
        INSTALLED_APPS = [
            ...
            'rest_framework',
            'rest_framework_simplejwt',
            ...
        ]

         REST_FRAMEWORK = {
             'DEFAULT_AUTHENTICATION_CLASSES': (
                 'rest_framework_simplejwt.authentication.JWTAuthentication',
             ),
         }

    ```

3.  Configurando o settings (`backend/mooney/mooney/routes/urls_api.py`)

    ```bash
        from django.urls import path, include
        from rest_framework import routers
        from apps.customer.api.v1.views import CustomerViewSet
        from rest_framework_simplejwt.views import (
            TokenObtainPairView,
            TokenRefreshView,
        )

        router = routers.DefaultRouter()
        router.register(r'customer', CustomerViewSet)

        urlpatterns = [
            path('v1/', include(router.urls)),
            path('v1/token/', TokenObtainPairView.as_view(), name="token_obtain_pair"),
            path('v1/token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
        ]
    ```

4.  Teste via curl

    ```bash
        curl --location 'http://api.mooney.com/v1/token/' \
        --header 'Content-Type: application/json' \
        --data '{
        "username": "mooney",
        "password": "mooney"
        }
        '
    ```

    Retorno

    ```bash
        {
            "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwNjk4NDY4NiwiaWF0IjoxNzA2ODk4Mjg2LCJqdGkiOiIyMGVhMjE3NzY0YzM0ZjBmYTYxNDdiMzNiOTZkMzM3MCIsInVzZXJfaWQiOjF9.2GgAE9_eWoQQ92zVfkqjbw_lQhEquj75fm9hyDqWSrg",
            "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA2ODk4NTg2LCJpYXQiOjE3MDY4OTgyODYsImp0aSI6ImI0N2U2OGRmYTI3MjQwMmM5OTg1Y2JhNmRmMGM5NTNmIiwidXNlcl9pZCI6MX0.EmRHAoHWVdpxoJYd6BiQnpcDrkgCTyu9xeHl-Xp0WaU"
        }
    ```

# OAuth2

1.  Pré-requisitos

        ```bash
            pip install django-oauth-toolkit
        ```

2.  Configurando o settings.py (base.py)

    ```bash
        INSTALLED_APPS = [
            ...
            'oauth2_provider',
            ...
        ]

         REST_FRAMEWORK = {
            'DEFAULT_AUTHENTICATION_CLASSES': (
                'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
            ),
        }

    ```

3.  Configurando o settings (`backend/mooney/mooney/routes/urls_api.py`)

    ```bash
        from django.urls import path, include
        from rest_framework import routers
        from apps.customer.api.v1.views import CustomerViewSet
        from rest_framework_simplejwt.views import (
            TokenObtainPairView,
            TokenRefreshView,
        )

        router = routers.DefaultRouter()
        router.register(r'customer', CustomerViewSet)

        urlpatterns = [
            path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
        ]
    ```

4.  Migrate
    ```bash
        python manage.py migrate oauth2_provider
    ```

- [Git](#instalacao-e-configuracao-do-git)
- [python](#instalacao-do-python)
- [Pip](#instalacao-do-pip)
- [Docker](#instalacao-e-configuracao-docker)
- [Docker Compose](#instalacao-e-configuracao-docker)

## Instalação e Configuração do Git

Se o Python 3 não estiver instalado, você pode instalá-lo usando:

```bash
sudo apt update
sudo apt install p
```
