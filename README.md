# Mooney Python Django API

## Objetivo

Projeto destinado a estudos e testes, por isso sempre á em constantes mudanças.
Consumo de API RESTful:
Autenticação JWT
Autenticação OAuth2
Autenticação Usuario Password
Gestão de Produto
Gestão de Cliente
Gestão de Venda

Gerenciar requisições de um fluxo de venda, partindo da criação da venda, adicionando produtos, selecionando cliente e vendedor, e finalizando na área de finanças onde o usuário poderá ver e gerenciar todas as entradas e parcelas realizadas pelas vendas.

## [Tecnologias Utilizadas](documentation/tecnologias.md)

- Python
- Django
- Docker
- API RESTful
- Nginx
- PostgreSQL
- Git Actions
- OAuth2
- Prometheus
- CAdvisor
- Grafana

## Conceitos Trabalhados

- Alguns conceitos de SOLID
- Design de Serviço
- MTV
- API RESTful
- Deploy Continuo
- Testes Automatizados
- Timezone
- Language
- Autenticação Token
- Autenticação OAuth2
- Subdominio

## Estrutura de Arquivos e Pastas

```
├── mooney-django/
│  ├── apps/
│  │  ├── account/
│  │  │  └── admin.py
│  │  │  ├── api/
│  │  │  │  └── __init__.py
│  │  │  │  ├── v1/
│  │  │  │  │  └── __init__.py
│  │  │  │  │  └── serializers.py
│  │  │  │  │  └── views.py
│  │  │  └── apps.py
│  │  │  └── __init__.py
│  │  │  └── models.py
│  │  │  └── tests.py
│  │  │  └── TimezoneMiddleware.py
│  │  │  └── UserLanguageMiddleware.py
│  │  │  └── views.py
│  │  ├── core/
│  │  │  ├── api/
│  │  │  │  ├── v1/
│  │  │  │  │  └── admin.py
│  │  │  │  │  └── apps.py
│  │  │  │  │  └── __init__.py
│  │  │  │  │  └── tests.py
│  │  │  │  │  └── views.py
│  │  │  └── apps.py
│  │  │  └── __init__.py
│  │  │  └── models.py
│  │  ├── customer/
│  │  │  └── admin.py
│  │  │  ├── api/
│  │  │  │  └── __init__.py
│  │  │  │  ├── v1/
│  │  │  │  │  └── admin.py
│  │  │  │  │  └── __init__.py
│  │  │  │  │  └── serializers.py
│  │  │  │  │  └── tests.py
│  │  │  │  │  └── views_oauth2_client_credentials.py
│  │  │  │  │  └── views_oauth2_password.py
│  │  │  │  │  └── views_oauth2.py
│  │  │  │  │  └── views.py
│  │  │  └── apps.py
│  │  │  └── __init__.py
│  │  │  └── models.py
│  │  │  └── tests.py
│  │  ├── erp/
│  │  │  └── __init__.py
│  │  │  ├── payment/
│  │  │  │  └── admin.py
│  │  │  │  ├── api/
│  │  │  │  │  ├── v1/
│  │  │  │  │  │  └── serializers.py
│  │  │  │  │  │  └── views.py
│  │  │  │  └── apps.py
│  │  │  │  └── __init__.py
│  │  │  │  └── models.py
│  │  │  │  └── tests.py
│  │  │  │  └── views.py
│  │  │  ├── transaction/
│  │  │  │  └── admin.py
│  │  │  │  ├── api/
│  │  │  │  │  └── __init__.py
│  │  │  │  │  ├── v1/
│  │  │  │  │  │  └── __init__.py
│  │  │  │  │  │  └── serializers.py
│  │  │  │  │  │  ├── services/
│  │  │  │  │  │  │  └── services.py
│  │  │  │  │  │  │  └── views.py
│  │  │  │  │  │  └── tests.py
│  │  │  │  │  │  └── views.py
│  │  │  │  └── apps.py
│  │  │  │  └── bk_tes.py
│  │  │  │  └── __init__.py
│  │  │  │  └── models.py
│  │  │  │  └── signals.py
│  │  │  │  └── tests.py
│  │  │  │  └── views.py
│  │  └── __init__.py
│  │  ├── product/
│  │  │  └── admin.py
│  │  │  ├── api/
│  │  │  │  └── __init__.py
│  │  │  │  ├── v1/
│  │  │  │  │  └── admin.py
│  │  │  │  │  └── __init__.py
│  │  │  │  │  └── serializers.py
│  │  │  │  │  └── tests.py
│  │  │  │  │  └── views_oauth2_client_credentials.py
│  │  │  │  │  └── views_oauth2_password.py
│  │  │  │  │  └── views_oauth2.py
│  │  │  │  │  └── views.py
│  │  │  └── apps.py
│  │  │  └── __init__.py
│  │  │  └── models.py
│  │  │  └── tests.py
│  │  │  └── views.py
│  │  ├── sale/
│  │  │  └── admin.py
│  │  │  ├── api/
│  │  │  │  └── __init__.py
│  │  │  │  ├── v1/
│  │  │  │  │  ├── factory/
│  │  │  │  │  │  └── factory.py
│  │  │  │  │  │  └── views.py
│  │  │  │  │  └── __init__.py
│  │  │  │  │  └── serializers.py
│  │  │  │  │  ├── strategies/
│  │  │  │  │  │  └── desconto.py
│  │  │  │  │  │  └── pagamento.py
│  │  │  │  │  │  └── views.py
│  │  │  │  │  └── tests.py
│  │  │  │  │  └── views.py
│  │  │  └── apps.py
│  │  │  └── __init__.py
│  │  │  └── models.py
│  │  │  └── tests.py
│  ├── config/
│  │  └── django-config.yaml
│  │  ├── local/
│  │  │  └── Dockerfile
│  │  │  └── entrypoint.sh
│  │  │  ├── nginx/
│  │  │  │  ├── conf.d/
│  │  │  │  │  └── mooney.conf
│  │  │  │  └── nginx_antigo.conf
│  │  │  │  └── nginx.conf
│  │  │  ├── postgres/
│  │  │  │  └── my-pg_hba.conf
│  │  │  │  └── my-postgresql.conf
│  │  │  │  └── pg_hba.conf
│  │  │  │  └── postgresql.conf
│  │  │  ├── postgresql/
│  │  │  │  ├── my-pg_hba.conf/
│  │  │  │  │  └── *
│  │  │  │  ├── my-postgresql.conf/
│  │  │  │  │  └── *
│  │  │  └── requirements.txt
│  │  ├── postgres/
│  │  │  ├── postgresql.conf/
│  │  │  │  └── *
│  │  ├── production/
│  │  │  └── *
│  │  ├── staging/
│  │  │  └── *
│  └── docker-compose.local.yml
│  └── docker-compose.production.yml
│  ├── k8s/
│  │  ├── configmaps/
│  │  │  └── configmap-django.yaml
│  │  │  └── configmap-nginx.yaml
│  │  │  └── configmap-postgres.yaml
│  │  │  └── configmap-prometheus.yaml
│  │  ├── cronjobs/
│  │  │  └── *
│  │  ├── deployments/
│  │  │  └── deployment-cadvisor.yml
│  │  │  └── deployment-django.yml
│  │  │  └── deployment-grafana.yml
│  │  │  └── deployment-nginx.yml
│  │  │  └── deployment-postgres.yml
│  │  │  └── deployment-prometheus.yml
│  │  ├── ingresses/
│  │  │  └── ingress.yaml
│  │  ├── jobs/
│  │  │  └── *
│  │  ├── secrets/
│  │  │  └── secret-django.yaml
│  │  ├── services/
│  │  │  └── service-cadvisor.yaml
│  │  │  └── service-django.yaml
│  │  │  └── service-grafana.yaml
│  │  │  └── service-nginx.yaml
│  │  │  └── service-postgres.yaml
│  │  │  └── service-prometheus.yaml
│  │  ├── volumes/
│  │  │  └── storageclass.yaml
│  │  │  └── volume-nginx.yaml
│  └── manage.py
│  ├── mooney/
│  │  └── asgi.py
│  │  └── base.py
│  │  └── __init__.py
│  │  └── local.py
│  │  ├── media/
│  │  │  └── *
│  │  └── production.py
│  │  ├── routes/
│  │  │  └── admin.py
│  │  │  ├── api/
│  │  │  │  ├── v1/
│  │  │  │  │  └── account.py
│  │  │  │  │  └── urls.py
│  │  │  └── hosts.py
│  │  │  └── metrics.py
│  │  │  └── root.py
│  │  │  └── urls_api.py
│  │  │  ├── urls_old/
│  │  │  │  └── admin.py
│  │  │  │  └── api.py
│  │  │  └── urls.py
│  │  └── settings.py
│  │  └── urls.py
│  │  └── wsgi.py
│  └── prometheus.yml
│  └── README.md
│  ├── tmp/
│  ├── tutorials/
│  │  ├── postman/
│  │  │  └── var-enviroment.md

```

## Passos para Executar o Projeto Localmente

### Pré-requisitos

- Git
- Python
- Pip
- Docker
- Docker Compose

### Ambiente de Testes

- Recomendado: Ubuntu

### Clonar o Repositório

```bash
git clone https://github.com/daniloftorres/mooney.github.io.git .
```

### Executar com Docker Compose

```bash
docker-compose -f docker-compose.local.yml up
```

Devera ver algo parecido com isso

```bash
CONTAINER ID   IMAGE                     COMMAND                  CREATED       STATUS       PORTS                                       NAMES
a2b4ebb3314e   nginx:latest              "/docker-entrypoint.…"   5 hours ago   Up 5 hours   0.0.0.0:80->80/tcp, :::80->80/tcp           mooney-django_nginx_1
aebd589d1ee1   mooney-django_django      "/entrypoint.sh"         5 hours ago   Up 5 hours   0.0.0.0:8000->8000/tcp, :::8000->8000/tcp   mooney-django_django_1
9b9cf0afaa42   grafana/grafana:latest    "/run.sh"                2 days ago    Up 5 hours   0.0.0.0:3000->3000/tcp, :::3000->3000/tcp   mooney-django_grafana_1
a2ba5b004fbf   postgres:14.1-alpine      "docker-entrypoint.s…"   3 days ago    Up 5 hours   0.0.0.0:5432->5432/tcp, :::5432->5432/tcp   mooney-django_postgres_1
2890c472db07   google/cadvisor:latest    "/usr/bin/cadvisor -…"   3 days ago    Up 5 hours   0.0.0.0:8080->8080/tcp, :::8080->8080/tcp   mooney-django_cadvisor_1
b434026e9b29   prom/prometheus:v2.26.0   "/bin/prometheus --c…"   3 days ago    Up 5 hours   0.0.0.0:9090->9090/tcp, :::9090->9090/tcp   mooney-django_prometheus_1
```

São 6 serviços principais rodando:

- Nginx

- Django

- Postgres

- prometheus

- CAdvisor

- Grafana

### Configuração de Hosts no Ubuntu

Adicione no arquivo `/etc/hosts` as configurações abaixo:

```bash
127.0.0.1 admin.mooney.com
127.0.0.1	api.mooney.com
127.0.0.1	django
127.0.0.1	prometheus
127.0.0.1	cadvisor
127.0.0.1	grafana
```

### Migrations iniciais.

Adicione no arquivo hosts as configurações abaixo:

```bash
docker exec -it mooney-django_django_1 python manage.py makemigrations
```

```bash
docker exec -it mooney-django_django_1 python manage.py migrate
```

```bash
remover-doc docker exec -it mooney-django-simulation_django_1 python manage.py makemigrations
remover-doc docker exec -it mooney-django-simulation_django_1 python manage.py migrate
```

### Configurações iniciais nos serviços

Adicione no arquivo hosts as configurações abaixo:

- Django

  - Vamos acessar o container para criar um super usuário
    #o usuario é apenas de exemplo, voce pode criar conforme preferir

  ```bash
  docker exec -it mooney-django_django_1 python manage.py createsuperuser
  ```

  - complete os dados pedido

    Username: mooney

    ```bash
    mooney
    ```

    Email: mooney@mooney.com

    ```bash
    mooney@mooney.com
    ```

    Password: mooney

    ```bash
    mooney
    ```

  - como nossa senha é pequena ele vai dar um alerta, para confirmar, apenas digite o y

    Password (again):mooney
    #The password is too similar to the username.
    #This password is too short. It must contain at least 8 characters.
    Bypass password validation and create user anyway? [y/N]: y

  - trecho admin remover
    remover-doc docker exec -it mooney-django-simulation_django_1 python manage.py createsuperuser
    echo "from django.contrib.auth.models import User; User.objects.create_superuser('mooney', 'email@example.com', 'password')" | python manage.py shell
    echo "from apps.account.models import CustomUser; CustomUser.objects.filter(username='mooney').delete()" | python manage.py shell

  - Tente acessar a url : http://admin.mooney.com/
    Se o login do admin django for exibido, tudo foi um sucesso ate agora.

# Monitoramento do Sistema e Observabilidade

## Prometheus

    - Para acessar o prometheus : http://prometheus:9090
    - Por default não precisa de usuario e senha
    - Cheque se as configurações de raspagem de dados configurada no `prometheus.yml` estão todas ativas corretamente.

    | Service    | Endpoint                      | State | Labels                   | Last Scrape  | Scrape Duration | Error         |
    |------------|-------------------------------|-------|--------------------------|--------------|----------------|---------------|
    | cadvisor   | http://cadvisor:8080/metrics  | UP    | instance="cadvisor:8080" job="cadvisor" | 416.000ms ago | 124.998ms       |               |
    | django     | http://django:8000/metrics    | UP    | instance="django:8000"   job="django"   | 6.869s ago   | 10.606ms        |               |
    | prometheus | http://localhost:9090/metrics | UP    | instance="localhost:9090" job="prometheus"| 8.266s ago   | 7.964ms         |               |

    - Todas tem que ter o State como UP

## CAdvisor

    - Para acessar o cadvisor : http://cadvisor:8080
    - Por default não precisa de usuario e senha
    - Deve exibir um dash com metricas em realtime da estrutura dos servidores do docker.

## Grafana

    - Para acessar o cadvisor : http://grafana:3000
    - Acesse com user : admin e password : admin

# API

Este documento fornece instruções sobre como acessar e interagir com a API Mooney, utilizando o framework Django. Abaixo estão listados os endpoints disponíveis e exemplos de requisições para cada um deles.

## Autenticação JWT

Para acessar a maioria dos endpoints, é necessário obter um token JWT e incluí-lo no cabeçalho das requisições.

### Obter Token JWT

```bash
curl --location --request POST 'http://api.mooney.com/v1/token/' \
--header 'Content-Type: application/json' \
--data-raw '{
"username": "mooney",
"password": "mooney"
}'
```

### Refresh Token JWT

```bash
curl --location --request POST 'http://api.mooney.com/v1/token/refresh/' \
--header 'Content-Type: application/json' \
--data-raw '{
"refresh": "{{refresh_token}}"
}
'
```

## Autenticação OAuth2

### Obter Token via Client Credentials

```bash
curl --location --request POST 'http://api.mooney.com/v1/oauth2/token/' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'client_id=76rpCwJqi34TCtR5euRlixQWBFfmt0zXYLvmYWDr' \
--data-urlencode 'client_secret=z63fKkzs9e3Ux22KlhnGvQNSYz1IIjdGr5OgIW228ZAmmebJckKyJPOzix4PfygE1VYrvf68KrT5BgqPyhPWolytvrcrSzXomXqgHA8u6xhILjwdqVHirPdMqVQESUCT' \
--data-urlencode 'grant_type=client_credentials'
```

### Obter Token via Password

```bash
curl --location --request POST 'http://api.mooney.com/v1/oauth2/token/' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'client_id=2LxBKN35djDbHhgvkMR7npMWWi0gKmtdlFyzVHQw' \
--data-urlencode 'client_secret=4FzCjVqfzipitUNMi3hZByGeRUDhDRkwCK9wVbJPN4CME8AxzGnh7KT6Gh6uMOBiCLexZ5EyBeLmPS1IVevpAlJjeionAUqRbZQQN9cG6NjTEtPdnNFDcnPw4znoPfK5' \
--data-urlencode 'username=mooney' \
--data-urlencode 'password=mooney' \
--data-urlencode 'grant_type=password'
```

## Postman

Algumas configurações para quem usa o Postman para testar as APIs. O conceito serve para outros programas similares.

- [Configuração básica para uso do Postman](documentation/postman/var-enviroment.md)

1. Criar Variaveis de Ambiente.
2. Configurar script para quando o request de obtenção do token tiver retorno, capturar o token para savar em nossa variavel de ambiente.
3. Adicionar a variavel de ambiente nas requests dentro do Authozitation : Bearer Token

## Cliente

### Criar Cliente

```bash
curl --location --request POST 'http://api.mooney.com/v1/customer/' \
--header 'Authorization: Bearer {{access_token}}' \
--header 'Content-Type: application/json' \
--data-raw '{
"name":"Danilo",
"email":"danilotorres@mail.com",
"phone":"16900001111"
}'
```

### Obter Cliente

```bash
curl --location --request GET 'http://api.mooney.com/v1/customer/1/' \
--header 'Authorization: Bearer {{access_token}}'
```

## Produto

### Criar Categoria de Produto

```bash
curl --location --request POST 'http://api.mooney.com/v1/product/category/' \
--header 'Authorization: Bearer {{access_token}}' \
--header 'Content-Type: application/json' \
--data-raw '[
{
"name": "Periféricos"
},
{
"name": "Componentes"
},
{
"name": "Acessórios"
}
]'
```

### Criar Produto

```bash
curl --location --request POST 'http://api.mooney.com/v1/product/' \
--header 'Authorization: Bearer {{access_token}}' \
--header 'Content-Type: application/json' \
--data-raw '[
{
"name": "Mouse Gamer RGB",
"description": "Mouse gamer com iluminação RGB e 7200 DPI.",
"price": "150",
"category_id": 1
},
{
"name": "Teclado Mecânico",
"description": "Teclado mecânico com switches azuis para melhor resposta tátil.",
"price": "300",
"category_id": 1
},
{
"name": "Headset 7.1 Surround",
"description": "Headset com som surround 7.1, microfone embutido e cancelamento de ruído.",
"price": "250",
"category_id": 1
},
{
"name": "Placa de Vídeo GTX 1660",
"description": "Placa de vídeo Nvidia GTX 1660 com 6GB de memória VRAM.",
"price": "2200",
"category_id": 2
},
{
"name": "Processador Ryzen 5 3600",
"description": "Processador AMD Ryzen 5 3600, 6 núcleos e 12 threads, até 4.2 GHz.",
"price": "1200",
"category_id": 2
},
{
"name": "SSD NVMe 1TB",
"description": "SSD NVMe com 1TB de capacidade e leituras de até 3500MB/s.",
"price": "900",
"category_id": 2
},
{
"name": "Memória RAM 16GB DDR4",
"description": "Kit de memória RAM DDR4, 16GB (2x8GB), 3200MHz.",
"price": "600",
"category_id": 2
},
{
"name": "Cabo USB Tipo-C",
"description": "Cabo USB Tipo-C de alta velocidade para carregamento e transferência de dados.",
"price": "50",
"category_id": 3
},
{
"name": "Capa Protetora para Notebook",
"description": "Capa protetora em neoprene para notebooks de até 15 polegadas.",
"price": "80",
"category_id": 3
},
{
"name": "Suporte para Monitor",
"description": "Suporte ajustável para monitor, com gestão de cabos integrada.",
"price": "150",
"category_id": 3
}
]'
```

### Obter Produto

```bash
curl --location --request GET 'http://api.mooney.com/v1/product/1/' \
--header 'Authorization: Bearer {{access_token}}'
```

## Método de Pagamento

### Criar Método de Pagamento

```bash
curl --location --request POST 'http://api.mooney.com/v1/payment/method/' \
--header 'Authorization: Bearer {{access_token}}' \
--header 'Content-Type: application/json' \
--data-raw '[
{
"payment_type": "CSH",
"description": "Pagamento em dinheiro"
},
{
"payment_type": "CHK",
"description": "Pagamento com cheque"
},
{
"payment_type": "CRC",
"description": "Pagamento com cartão de crédito"
},
{
"payment_type": "DBT",
"description": "Pagamento com cartão de débito"
},
{
"payment_type": "BKT",
"description": "Transferência bancária"
},
{
"payment_type": "BLT",
"description": "Pagamento via boleto"
},
{
"payment_type": "PIX",
"description": "Pagamento via PIX"
},
{
"payment_type": "EWT",
"description": "Pagamento via carteira digital"
}
]'
```

### Obter Método de Pagamento

```bash
curl --location --request GET 'http://api.mooney.com/v1/payment/method/1/' \
--header 'Authorization: Bearer {{access_token}}'
```

## Transação de Venda

### Criar Transação de Venda

```bash
curl --location --request POST 'http://api.mooney.com/v1/service/sale/' \
--header 'Authorization: Bearer {{access_token}}' \
--header 'Content-Type: application/json' \
--data-raw '{
"status": "creation",
"user": 1,
"seller": 1,
"customer": 1
}'
```

### Obter Transação de Venda

```bash
curl --location --request GET 'http://api.mooney.com/v1/sale/10/' \
--header 'Authorization: Bearer {{access_token}}'
```

### Update Transação de Venda

```bash
curl --location --request PUT 'http://api.mooney.com/v1/service/sale/1/' \
--header 'Authorization: Bearer {{access_token}}' \
--header 'Content-Type: application/json' \
--data-raw '{
"id": 1,
"customer": 1,
"user": 1,
"seller": 1,
"sale_transaction_status": "billing",
"sale_transaction_type": "expense"
}'
```

## Transação de Venda Item

### Criar Transação de Venda Item

```bash
curl --location --request POST 'http://api.mooney.com/v1/service/sale/item/' \
--header 'Authorization: Bearer {{access_token}}' \
--header 'Content-Type: application/json' \
--data-raw '{
"quantity": 5,
"discount":10,
"sale_price": "50.00",
"sale_transaction": 1,
"product": 1
}'
```

### Atualizar Transação de Venda Item

```bash
curl --location --request PUT 'http://api.mooney.com/v1/service/sale/item/1/' \
--header 'Authorization: Bearer {{access_token}}' \
--header 'Content-Type: application/json' \
--data-raw '{
"quantity": 5,
"discount":10,
"sale_price": "50.00",
"sale_transaction": 1,
"product": 1
}'
```

### Obter Transação de Venda Item

```bash
curl --location --request GET 'http://api.mooney.com/v1/sale/item/1/' \
--header 'Authorization: Bearer {{access_token}}'
```

### Remover Transação de Venda Item

```bash
curl --location --request DELETE 'http://api.mooney.com/v1/service/sale/item/1/' \
--header 'Authorization: Bearer {{access_token}}
```

## Método de Pagamento para a Transação de Venda

### Criar Método de Pagamento para a Transação de Venda

```bash
curl --location --request POST 'http://api.mooney.com/v1/service/sale/payment/' \
--header 'Authorization: Bearer {{access_token}}' \
--header 'Content-Type: application/json' \
--data-raw '{
"sale_transaction": 2,
"payment_method": 3,
"total_amount": "100",
"installment": 1,
"payer_cpf_cnpj":"",
"number":"",
"name_card_holder":""
}'
```

### Atualizar Método de Pagamento para a Transação de Venda

```bash
curl --location --request PUT 'http://api.mooney.com/v1/service/sale/payment/1/' \
--header 'Authorization: Bearer {{access_token}}' \
--header 'Content-Type: application/json' \
--data-raw '{
"quantity": 5,
"discount":10,
"sale_price": "50.00",
"sale_transaction": 1,
"product": 1
}'
```

### Obter Método de Pagamento para a Transação de Venda

```bash
curl --location --request GET 'http://api.mooney.com/v1/service/sale/payment/1/' \
--header 'Authorization: Bearer {{access_token}}'
```

### Remover Método de Pagamento para a Transação de Venda

```bash
curl --location --request DELETE 'http://api.mooney.com/v1/service/sale/payment/1/' \
--header 'Authorization: Bearer {{access_token}}'
```
