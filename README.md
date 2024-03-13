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
  - Obter Sale Transaction

- **Sale Transaction Item**

  - Criar Sale Transaction Item
  - Obter Sale Transaction Item

- **Product**

  - Listar ou Criar Produto

- **Payment Method**
  - Criar Método de Pagamento

## Documentação de Acesso

Para mais detalhes sobre como acessar e interagir com a Mooney API, consulte a documentação completa.
