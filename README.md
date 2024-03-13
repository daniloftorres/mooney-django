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

## Estrutura de Arquivos e Pastas

```
<detalhe da estrutura de arquivos omitido para brevidade>
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

## Autenticação e Uso da API

### Autenticação JWT

- **Obter Token JWT**

  ```bash
  curl -X POST http://localhost:8000/v1/token/        -H "Content-Type: application/json"        -d '{"username": "seu_usuario", "password": "sua_senha"}'
  ```

- **Refresh Token JWT**
  ```bash
  curl -X POST http://localhost:8000/v1/token/refresh/        -H "Content-Type: application/json"        -d '{"refresh": "seu_refresh_token"}'
  ```

### Autenticação OAuth2

- **Obter Token via Client Credentials**

  ```bash
  curl -X POST http://localhost:8000/v1/oauth2-client-credentials/        -H "Authorization: Basic <base64(client_id:client_secret)>"        -d "grant_type=client_credentials"
  ```

- **Obter Token via Password**
  ```bash
  curl -X POST http://localhost:8000/v1/oauth2-password/        -H "Authorization: Basic <base64(client_id:client_secret)>"        -d "grant_type=password&username=seu_usuario&password=sua_senha"
  ```

### Exemplos de Uso da API

- **Sale Transaction**

  - Criar Sale Transaction

  ```bash

  ```

  - Obter Sale Transaction

- **Sale Transaction Item**

  - Criar Sale Transaction Item
  - Obter Sale Transaction Item

- **Product**

  - Listar ou Criar Produto

- **Payment Method**
  - Criar Método de Pagamento

# Mooney API - Documentação de Acesso

Este documento fornece instruções sobre como acessar e interagir com a Mooney API, utilizando o framework Django. Abaixo estão listados os endpoints disponíveis e exemplos de como fazer requisições para cada um deles.

## Autenticação JWT

Para acessar a maioria dos endpoints, é necessário obter um token JWT e incluí-lo no cabeçalho das suas requisições.

### Obter Token JWT

```bash
curl -X POST http://localhost:8000/v1/token/ \
     -H "Content-Type: application/json" \
     -d '{"username": "seu_usuario", "password": "sua_senha"}'
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
curl -X POST http://localhost:8000/v1/oauth2-client-credentials/ \
     -H "Authorization: Basic <base64(client_id:client_secret)>" \
     -d "grant_type=client_credentials"
```

### Obter Token via Password

```bash
curl -X POST http://localhost:8000/v1/oauth2-password/ \
     -H "Authorization: Basic <base64(client_id:client_secret)>" \
     -d "grant_type=password&username=seu_usuario&password=sua_senha"
```

## Sale Transaction

### Criar Sale Transaction

```bash
curl -X POST http://localhost:8000/v1/service/sale/ \
     -H "Authorization: Bearer seu_access_token" \
     -H "Content-Type: application/json" \
     -d '{"campo": "valor", "outro_campo": "outro_valor"}'
```

### Obter Sale Transaction

```bash
curl -X GET http://localhost:8000/v1/service/sale/<int:pk>/ \
     -H "Authorization: Bearer seu_access_token"
```

## Sale Transaction Item

### Criar Sale Transaction Item

```bash
curl -X POST http://localhost:8000/v1/service/sale/item/ \
     -H "Authorization: Bearer seu_access_token" \
     -H "Content-Type: application/json" \
     -d '{"produto": produto_id, "quantidade": quantidade, "sale_price": preço}'
```

### Obter Sale Transaction Item

```bash
curl -X GET http://localhost:8000/v1/service/sale/item/<int:pk>/ \
     -H "Authorization: Bearer seu_access_token"
```

## Product

### Listar ou Criar Produto

```bash
curl -X GET http://localhost:8000/v1/product/ \
     -H "Authorization: Bearer seu_access_token"
```

```bash
curl -X POST http://localhost:8000/v1/product/ \
     -H "Authorization: Bearer seu_access_token" \
     -H "Content-Type: application/json" \
     -d '{"nome": "Nome do Produto", "categoria": categoria_id, ...}'
```

## Payment Method

### Criar Método de Pagamento

```bash
curl -X POST http://localhost:8000/v1/payment/method/ \
     -H "Authorization: Bearer seu_access_token" \
     -H "Content-Type: application/json" \
     -d '{"tipo": "Tipo de Pagamento", "detalhes": "Detalhes do Pagamento"}'
```

Substitua `"seu_access_token"`, `"seu_refresh_token"`, `"seu_usuario"`, `"sua_senha"`, `"produto_id"`, `"quantidade"`, `"preço"`, `"categoria_id"`, `"Tipo de Pagamento"`, `"Detalhes do Pagamento"`, e outros campos necessários conforme apropriado para suas requisições específicas.
