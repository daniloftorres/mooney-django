# Mooney Python API

## Objetivo

Gerenciar requisições de um fluxo de venda, partindo da criação da venda, adicionando produtos, selecionando cliente e vendedor, e finalizando na área de finanças onde o usuário poderá ver e gerenciar todas as entradas e parcelas realizadas pelas vendas.

## Tecnologias Utilizadas

- Python
- Django
- Docker
- API REST

## Conceitos Trabalhados

- Alguns conceitos de SOLID
- Design de Serviço
- MTV
- API REST

## Estrutura de Arquivos e Pastas

```
├── mooney-django/
│   ├── apps/
│   │   ├── account/
│   │   │   └── admin.py
│   │   │   ├── api/
│   │   │   │   └── __init__.py
│   │   │   │   ├── v1/
│   │   │   │   │   └── __init__.py
│   │   │   │   │   └── serializers.py
│   │   │   │   │   └── views.py
│   │   │   └── apps.py
│   │   │   └── __init__.py
│   │   │   ├── migrations/
│   │   │   │   └── 0001_initial.py
│   │   │   │   └── __init__.py
│   │   │   └── models.py
│   │   │   └── tests.py
│   │   │   └── TimezoneMiddleware.py
│   │   │   └── UserLanguageMiddleware.py
│   │   │   └── views.py
│   │   ├── core/
│   │   │   ├── api/
│   │   │   │   ├── v1/
│   │   │   │   │   └── admin.py
│   │   │   │   │   └── apps.py
│   │   │   │   │   └── __init__.py
│   │   │   │   │   ├── migrations/
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   └── tests.py
│   │   │   │   │   └── views.py
│   │   │   └── apps.py
│   │   │   └── __init__.py
│   │   │   ├── migrations/
│   │   │   │   └── __init__.py
│   │   │   └── models.py
│   │   ├── customer/
│   │   │   └── admin.py
│   │   │   ├── api/
│   │   │   │   └── __init__.py
│   │   │   │   ├── v1/
│   │   │   │   │   └── admin.py
│   │   │   │   │   └── __init__.py
│   │   │   │   │   └── serializers.py
│   │   │   │   │   └── tests copy.py
│   │   │   │   │   └── tests.py
│   │   │   │   │   └── views_oauth2_client_credentials.py
│   │   │   │   │   └── views_oauth2_password.py
│   │   │   │   │   └── views_oauth2.py
│   │   │   │   │   └── views.py
│   │   │   └── apps.py
│   │   │   └── __init__.py
│   │   │   ├── migrations/
│   │   │   │   └── 0001_initial.py
│   │   │   │   └── __init__.py
│   │   │   └── models.py
│   │   │   └── tests.py
│   │   ├── erp/
│   │   │   ├── payment/
│   │   │   │   └── admin.py
│   │   │   │   ├── api/
│   │   │   │   │   ├── v1/
│   │   │   │   │   │   └── serializers.py
│   │   │   │   │   │   └── views.py
│   │   │   │   └── apps.py
│   │   │   │   └── __init__.py
│   │   │   │   ├── migrations/
│   │   │   │   │   └── 0001_initial.py
│   │   │   │   │   └── __init__.py
│   │   │   │   └── models.py
│   │   │   │   └── tests.py
│   │   │   │   └── views.py
│   │   │   ├── transaction/
│   │   │   │   └── admin.py
│   │   │   │   ├── api/
│   │   │   │   │   └── __init__.py
│   │   │   │   │   ├── v1/
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   └── serializers.py
│   │   │   │   │   │   ├── services/
│   │   │   │   │   │   │   └── services.py
│   │   │   │   │   │   │   └── views.py
│   │   │   │   │   │   └── tests.py
│   │   │   │   │   │   └── views.py
│   │   │   │   └── apps.py
│   │   │   │   └── __init__.py
│   │   │   │   ├── migrations/
│   │   │   │   │   └── 0001_initial.py
│   │   │   │   │   └── 0002_auto_20240311_1802.py
│   │   │   │   │   └── 0003_alter_saletransaction_sale_date.py
│   │   │   │   │   └── 0004_alter_paymentinstallmentsaletransaction_status.py
│   │   │   │   │   └── 0005_alter_paymentinstallmentsaletransaction_installment.py
│   │   │   │   │   └── 0006_auto_20240312_0044.py
│   │   │   │   │   └── 0007_saletransaction_total_quantity.py
│   │   │   │   │   └── __init__.py
│   │   │   │   └── models.py
│   │   │   │   └── signals.py
│   │   │   │   └── tests.py
│   │   │   │   └── views.py
│   │   ├── product/
│   │   │   └── admin.py
│   │   │   ├── api/
│   │   │   │   └── __init__.py
│   │   │   │   ├── v1/
│   │   │   │   │   └── admin.py
│   │   │   │   │   └── __init__.py
│   │   │   │   │   └── serializers.py
│   │   │   │   │   └── tests copy.py
│   │   │   │   │   └── tests.py
│   │   │   │   │   └── views_oauth2_client_credentials.py
│   │   │   │   │   └── views_oauth2_password.py
│   │   │   │   │   └── views_oauth2.py
│   │   │   │   │   └── views.py
│   │   │   └── apps.py
│   │   │   └── __init__.py
│   │   │   ├── migrations/
│   │   │   │   └── 0001_initial.py
│   │   │   │   └── __init__.py
│   │   │   └── models.py
│   │   │   └── tests.py
│   │   │   └── views.py
│   │   ├── sale/
│   │   │   └── admin.py
│   │   │   ├── api/
│   │   │   │   └── __init__.py
│   │   │   │   ├── v1/
│   │   │   │   │   ├── factory/
│   │   │   │   │   │   └── factory.py
│   │   │   │   │   │   └── views.py
│   │   │   │   │   └── __init__.py
│   │   │   │   │   └── serializers.py
│   │   │   │   │   ├── strategies/
│   │   │   │   │   │   └── desconto.py
│   │   │   │   │   │   └── pagamento.py
│   │   │   │   │   │   └── views.py
│   │   │   │   │   └── tests.py
│   │   │   │   │   └── views.py
│   │   │   └── apps.py
│   │   │   └── __init__.py
│   │   │   ├── migrations/
│   │   │   │   └── __init__.py
│   │   │   └── models.py
│   │   │   └── tests.py
│   └── clear_database.py
│   ├── config/
│   │   ├── local/
│   │   │   └── Dockerfile
│   │   │   └── entrypoint.sh
│   │   │   ├── nginx/
│   │   │   │   ├── conf.d/
│   │   │   │   │   └── mooney.conf
│   │   │   │   └── nginx_antigo.conf
│   │   │   │   └── nginx.conf
│   │   │   ├── postgres/
│   │   │   │   └── my-pg_hba.conf
│   │   │   │   └── my-postgresql.conf
│   │   │   │   └── postgresql.conf
│   │   │   ├── postgresql/
│   │   │   │   ├── my-pg_hba.conf/
│   │   │   │   │   └── *
│   │   │   │   ├── my-postgresql.conf/
│   │   │   │   │   └── *
│   │   │   └── requirements.txt
│   │   ├── postgres/
│   │   │   ├── postgresql.conf/
│   │   │   │   └── *
│   │   ├── production/
│   │   │   └── *
│   │   ├── staging/
│   │   │   └── *
│   └── docker-compose.local.yml
│   └── docker-compose.production.yml
│   └── draw_tree.sh
│   └── manage.py
│   ├── mooney/
│   │   └── asgi.py
│   │   └── base.py
│   │   └── __init__.py
│   │   └── local.py
│   │   ├── media/
│   │   │   └── *
│   │   └── production.py
│   │   ├── routes/
│   │   │   └── admin.py
│   │   │   ├── api/
│   │   │   │   ├── v1/
│   │   │   │   │   └── account.py
│   │   │   │   │   └── urls.py
│   │   │   └── hosts.py
│   │   │   └── urls_api.py
│   │   │   ├── urls_old/
│   │   │   │   └── admin.py
│   │   │   │   └── api.py
│   │   │   └── urls.py
│   │   └── settings.py
│   │   └── urls.py
│   │   └── wsgi.py
│   └── README.md
│   └── remove_migrations.sh
│   └── structure.txt

```

## Passos para Executar o Projeto Localmente

### Pré-requisitos

- Git
- Python
- Pip
- Docker
- Docker Compose

### Ambiente de Testes

- Ubuntu

### Clonar o Repositório

```bash
git clone https://github.com/daniloftorres/mooney.github.io.git
```

### Executar com Docker Compose

```bash
     docker-compose -f docker-compose.local.yml up
```

### Configuração de Hosts no Ubuntu

Adicione no arquivo hosts as configurações abaixo:

```
     127.0.0.1       admin.mooney.com
     127.0.0.1       api.mooney.com
```

# Documentação de Acesso

Este documento fornece instruções sobre como acessar e interagir com a Mooney API, utilizando o framework Django. Abaixo estão listados os endpoints disponíveis e exemplos de como fazer requisições para cada um deles.

## Autenticação JWT

Para acessar a maioria dos endpoints, é necessário obter um token JWT e incluí-lo no cabeçalho das suas requisições.

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
curl -X POST http://localhost:8000/v1/token/refresh/ \
     -H "Content-Type: application/json" \
     -d '{"refresh": "seu_refresh_token"}'
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

## Sale Transaction

### Criar Sale Transaction

```bash
     curl --location --request POST 'http://api.mooney.com/v1/sale/' \
     --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzEwMjczNTQzLCJpYXQiOjE3MTAyNzMyNDMsImp0aSI6ImY5OGU4N2FmNjk3YTQ0NmZhMzY2MTQzMWM1ZGRkOGY0IiwidXNlcl9pZCI6MX0.1ZgBgbU65J6m6adQOrf7bIDc3Iyk1zhT9_o7OeJOpkk' \
     --header 'Content-Type: application/json' \
     --data-raw '{
     "status": "creation",
     "user": 1,
     "seller": 1,
     "customer": 1,
     "total_price": 90.00,
     "total_discount": 10.00,
     "total_amount":0.00,
     "net_amount":0.00,
     "total_discount_amount":0.00,
     "items": [
          {
               "product": 4,
               "quantity": 2,
               "sale_price": 50.00,
               "discount":10,
               "amount":45.00
          },
          {
               "product": 5,
               "quantity": 1,
               "sale_price": 50.00,
               "discount":10,
               "amount":45.00
          }
          ]
     }'
```

### Obter Sale Transaction

```bash
     curl --location --request GET 'http://api.mooney.com/v1/sale/10/' \
     --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzEwMjczNTQzLCJpYXQiOjE3MTAyNzMyNDMsImp0aSI6ImY5OGU4N2FmNjk3YTQ0NmZhMzY2MTQzMWM1ZGRkOGY0IiwidXNlcl9pZCI6MX0.1ZgBgbU65J6m6adQOrf7bIDc3Iyk1zhT9_o7OeJOpkk'
```

## Sale Transaction Item

### Criar Sale Transaction Item

```bash
     curl --location --request POST 'http://api.mooney.com/v1/sale/item/' \
     --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzEwMjczNTQzLCJpYXQiOjE3MTAyNzMyNDMsImp0aSI6ImY5OGU4N2FmNjk3YTQ0NmZhMzY2MTQzMWM1ZGRkOGY0IiwidXNlcl9pZCI6MX0.1ZgBgbU65J6m6adQOrf7bIDc3Iyk1zhT9_o7OeJOpkk' \
     --header 'Content-Type: application/json' \
     --data-raw '{
     "sale_transaction_id": 10,
     "quantity": 5,
     "discount":10,
     "sale_price": "50.00",
     "sale_transaction": 10,
     "product": 4
     }'
```

### Obter Sale Transaction Item

```bash
     curl --location --request GET 'http://api.mooney.com/v1/sale/item/11/' \
     --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzEwMjczNTQzLCJpYXQiOjE3MTAyNzMyNDMsImp0aSI6ImY5OGU4N2FmNjk3YTQ0NmZhMzY2MTQzMWM1ZGRkOGY0IiwidXNlcl9pZCI6MX0.1ZgBgbU65J6m6adQOrf7bIDc3Iyk1zhT9_o7OeJOpkk'
```

## Product

### Criar Produto

```bash
     curl --location --request POST 'http://api.mooney.com/v1/product/' \
     --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzEwMjczNTQzLCJpYXQiOjE3MTAyNzMyNDMsImp0aSI6ImY5OGU4N2FmNjk3YTQ0NmZhMzY2MTQzMWM1ZGRkOGY0IiwidXNlcl9pZCI6MX0.1ZgBgbU65J6m6adQOrf7bIDc3Iyk1zhT9_o7OeJOpkk' \
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
          }
     ]'
```

## Criar Categoria de Produto

```bash
     curl --location --request POST 'http://api.mooney.com/v1/product/category/' \
     --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzEwMjczNTQzLCJpYXQiOjE3MTAyNzMyNDMsImp0aSI6ImY5OGU4N2FmNjk3YTQ0NmZhMzY2MTQzMWM1ZGRkOGY0IiwidXNlcl9pZCI6MX0.1ZgBgbU65J6m6adQOrf7bIDc3Iyk1zhT9_o7OeJOpkk' \
     --header 'Content-Type: application/json' \
     --data-raw '{
     "name": "Acessórios"
     }
     '
```

## Payment Method

### Criar Método de Pagamento

```bash
     curl --location --request POST 'http://api.mooney.com/v1/payment/method/' \
     --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzEwMjczNTQzLCJpYXQiOjE3MTAyNzMyNDMsImp0aSI6ImY5OGU4N2FmNjk3YTQ0NmZhMzY2MTQzMWM1ZGRkOGY0IiwidXNlcl9pZCI6MX0.1ZgBgbU65J6m6adQOrf7bIDc3Iyk1zhT9_o7OeJOpkk' \
     --header 'Content-Type: application/json' \
     --data-raw '[
          {
               "payment_type": "CSH",
               "description": "Pagamento em dinheiro"
          },
          {
               "payment_type": "CHK",
               "description": "Pagamento com cheque"
          }
     ]'
```

### Obter Método de Pagamento

```bash
     curl --location --request GET 'http://api.mooney.com/v1/payment/method/1/' \
     --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzEwMjczNTQzLCJpYXQiOjE3MTAyNzMyNDMsImp0aSI6ImY5OGU4N2FmNjk3YTQ0NmZhMzY2MTQzMWM1ZGRkOGY0IiwidXNlcl9pZCI6MX0.1ZgBgbU65J6m6adQOrf7bIDc3Iyk1zhT9_o7OeJOpkk'
```
