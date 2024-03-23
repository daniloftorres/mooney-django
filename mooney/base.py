"""
Django settings for mooney project.

Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
# from decouple import Config, RepositoryEnv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Caminho para o arquivo .env
# env_path = 'mooney/.env'

# Carrega as variáveis de ambiente do arquivo .env
# config = Config(RepositoryEnv(env_path))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-*gq8)xj3ufyb#myla^9isdr4p44oe5pgb7t)%7i(i&&3@42q(e'
# print("GET DADOS DB ENV SECRET_KEY:: ", os.getenv('SECRET_KEY'))
SECRET_KEY = os.getenv('SECRET_KEY')
print("######")
print("## SECRET_KEY :: ", SECRET_KEY)
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
# ROOT_HOSTCONF = 'mooney.mooney.routes.hosts'
DEFAULT_HOST = 'admin-django'


# Application definition

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
    'oauth2_provider',
    'django_prometheus',

    # ... mooney apps
    'apps.account',
    'apps.core',
    'apps.customer',
    'apps.product',
    # 'apps.sale',
    'apps.erp.payment',
    'apps.erp.transaction.apps.TransactionConfig',
]

MIDDLEWARE = [
    'django_prometheus.middleware.PrometheusBeforeMiddleware',

    'django_hosts.middleware.HostsRequestMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'apps.account.TimezoneMiddleware.TimezoneMiddleware',
    'apps.account.UserLanguageMiddleware.UserLanguageMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_hosts.middleware.HostsResponseMiddleware',

    'django_prometheus.middleware.PrometheusAfterMiddleware',
]
if DEBUG:
    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework_simplejwt.authentication.JWTAuthentication',
            'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
        ),


        'DEFAULT_PERMISSION_CLASSES': (
            'rest_framework.permissions.IsAuthenticated',
        ),

        'DEFAULT_RENDERER_CLASSES': [
            'rest_framework.renderers.JSONRenderer',
            'rest_framework.renderers.BrowsableAPIRenderer',
        ],
    }
else:
    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework_simplejwt.authentication.JWTAuthentication',
            'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
        ),


        'DEFAULT_PERMISSION_CLASSES': (
            'rest_framework.permissions.IsAuthenticated',
        ),
    }

# Defina os idiomas que seu site suportará
LANGUAGES = [
    ('en', 'English'),
    ('pt-br', 'Português Brasileiro'),
    # Adicione mais conforme necessário
]

# Caminho para os diretórios onde os arquivos de tradução serão armazenados
# LOCALE_PATHS = [BASE_DIR / 'locale/',]
LOCALE_PATHS = [os.path.join(BASE_DIR, 'mooney/static/locale'),]
# Defina o idioma padrão para o site
LANGUAGE_CODE = 'en-us'

# Use o fuso horário do usuário
USE_I18N = True

# Use datas e números localizados
USE_L10N = True

# teste
# ROOT_URLCONF = 'mooney.routes.urls'
ROOT_URLCONF = 'mooney.routes.urls_api'
ROOT_URLADMIN = 'mooney.routes.admin'
ROOT_HOSTCONF = 'mooney.routes.hosts'
# ROOT_HOSTDOC = 'mooney.routes.doc'
# DEFAULT_HOST = 'www'
# ROOT_HOSTCONF = 'meuprojeto.hosts'

AUTH_USER_MODEL = 'account.CustomUser'
OAUTH2_PROVIDER = {
    # Tempo de vida do token de acesso em segundos.
    'ACCESS_TOKEN_EXPIRE_SECONDS': 36000,  # Por exemplo, 10 horas.

    # Tempo de vida do token de atualização em segundos.
    'REFRESH_TOKEN_EXPIRE_SECONDS': 86400,  # Por exemplo, 1 dia.

    # Escopo padrão atribuído aos novos tokens.
    'SCOPES': {'read': 'Ler acesso', 'write': 'Acesso de escrita', 'groups': 'Acesso a grupos'},

    # Política de rotação de tokens, True significa que o token de atualização será renovado com cada solicitação.
    'ROTATE_REFRESH_TOKEN': False,  # ou True para habilitar a rotação.

    # Define se apenas tokens de acesso seguros (HTTPS) são emitidos.
    # ou False em ambientes de desenvolvimento sem HTTPS.
    'REQUIRE_SECURE_TRANSPORT': True,

    # Período de tempo para o qual o código de autorização é válido (em segundos).
    'AUTHORIZATION_CODE_EXPIRE_SECONDS': 300,  # Por exemplo, 5 minutos.

    # Definição de aplicativo de cliente padrão, como 'confidential' ou 'public'.
    'DEFAULT_APPLICATIONS': {
        'client_type': 'confidential',
        'authorization_grant_type': 'authorization-code',
    },

    # Define o caminho para uma função que deve gerar o token de acesso.
    # 'ACCESS_TOKEN_GENERATOR': 'path.to.custom.access_token.generator',

    # Define se o escopo do token de acesso deve ser exibido durante a autorização.
    'REQUEST_APPROVAL_PROMPT': 'force',

    # Outras configurações...
}


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mooney.wsgi.application'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

"""DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}"""

DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': os.getenv('POSTGRES_DB', os.path.join(BASE_DIR, 'db.sqlite3')),
        'USER': os.getenv('POSTGRES_USER', ''),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', ''),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': os.getenv('DB_PORT', ''),
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django_prometheus.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

# STATIC_URL = '/static/'
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

TEST_RUNNER = 'django.test.runner.DiscoverRunner'
