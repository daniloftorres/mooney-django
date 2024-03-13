# Mooney Python API

## Overview

Mooney Python API é uma aplicação construída para gerenciar o fluxo completo de vendas, desde a criação da venda, adição de produtos, seleção de clientes e vendedores, até a finalização na área de finanças. Na área financeira, os usuários podem visualizar e gerenciar todas as entradas e parcelas resultantes das vendas. Este projeto aplica conceitos de SOLID e Design de Serviço para criar uma solução robusta e escalável.

## Tecnologias Utilizadas

- Python
- Django
- Django Rest Framework
- Docker
- API REST

## Conceitos

- SOLID Principles
- Design de Serviço
- Autenticação e Autorização
- Trabalho com Docker e Docker Compose

## Estrutura de Arquivos e Pastas

A estrutura do projeto segue um modelo modular, facilitando a compreensão e manutenção do código. Cada módulo é responsável por uma parte específica da lógica de negócio, organizados da seguinte forma:

```
mooney/
├── apps/
│   ├── account/
│   ├── core/
│   ├── customer/
│   ├── erp/
│   │   ├── payment/
│   │   └── transaction/
│   └── product/
├── config/
│   ├── local/
│   └── production/
├── mooney/
│   ├── asgi.py
│   ├── settings.py
│   └── urls.py
└── docker-compose.yml
```

## Como Executar o Projeto Localmente

### Pré-requisitos

- Git
- Python 3.x
- Pip
- Docker
- Docker Compose

### Configuração do Ambiente

O projeto foi testado em um ambiente Ubuntu, mas pode ser executado em qualquer sistema operacional que suporte as tecnologias utilizadas.

### Clonando o Projeto

```bash
git clone https://github.com/daniloftorres/mooney.github.io.git
```

### Executando com Docker Compose

```bash
docker-compose -f docker-compose.local.yml up
```

### Configuração do Hosts no Ubuntu

Adicione as seguintes linhas ao arquivo `/etc/hosts`:

```
127.0.0.1       admin.mooney.com
127.0.0.1       api.mooney.com
```

### Checagem do Sistema

Após iniciar os serviços com Docker Compose, você pode acessar a API em `http://api.mooney.com` e o painel de administração em `http://admin.mooney.com`.

## Utilizando a API

A Mooney API utiliza autenticação JWT para a maioria dos endpoints. É necessário obter um token JWT e incluí-lo no cabeçalho das requisições para acessar os recursos protegidos.

### Exemplos de Requisições

A documentação detalhada para interagir com cada endpoint está disponível na documentação da API, que pode ser acessada após iniciar o projeto. Seguem alguns exemplos de como utilizar os endpoints principais:

- **Obter Token JWT:**

```bash
curl -X POST http://api.mooney.com/v1/token/      -H "Content-Type: application/json"      -d '{"username": "seu_usuario", "password": "sua_senha"}'
```

- **Criar Sale Transaction:**

```bash
curl -X POST http://api.mooney.com/v1/service/sale/      -H "Authorization: Bearer seu_access_token"      -H "Content-Type: application/json"      -d '{"customer": "id_do_cliente", "seller": "id_do_vendedor", ...}'
```
