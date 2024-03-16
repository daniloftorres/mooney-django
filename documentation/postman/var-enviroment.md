# Criar Variáveis de Ambiente no Postman

Este tutorial ensina como criar e usar variáveis de ambiente no Postman, tornando suas coleções mais dinâmicas e fáceis de manter. As variáveis de ambiente são úteis para armazenar valores que variam entre diferentes ambientes, como URLs base, credenciais de autenticação e outros dados.

## Índice

- [Passo 1: Acessar a Gestão de Ambientes](#passo-1-acessar-a-gestão-de-ambientes)
- [Passo 2: Criar um Novo Ambiente](#passo-2-criar-um-novo-ambiente)
- [Passo 3: Adicionar Variáveis ao Ambiente](#passo-3-adicionar-variáveis-ao-ambiente)
- [Passo 4: Salvar e Utilizar o Ambiente](#passo-4-salvar-e-utilizar-o-ambiente)
- [Passo 5: Usar Variáveis nas Requisições](#passo-5-usar-variáveis-nas-requisições)

## Passo 1: Acessar a Gestão de Ambientes

1. Abra o **Postman**.
2. No canto superior direito, clique no ícone de engrenagem chamado **"Settings"**.
3. Selecione **"Manage Environments"**. Uma nova janela se abrirá.

## Passo 2: Criar um Novo Ambiente

1. Na janela **"Manage Environments"**, clique no botão **"Add"** para criar um novo ambiente.
2. Nomeie seu ambiente. Esse nome pode ser qualquer coisa que faça sentido para você, como "Desenvolvimento", "Produção", etc.

## Passo 3: Adicionar Variáveis ao Ambiente

1. Com o ambiente nomeado, você definirá as variáveis. Você verá três campos para cada variável: **"Variable"** (nome da variável), **"Initial Value"** (valor inicial), e **"Current Value"** (valor atual).
2. No campo **"Variable"**, insira o nome da variável que deseja criar (e.g., `base_url`).
3. No campo **"Initial Value"**, insira o valor que essa variável terá (e.g., `https://api.minhaempresa.com`).
4. Opcionalmente, insira o mesmo ou um valor diferente no campo **"Current Value"**. O "Current Value" pode ser alterado durante o uso do Postman sem afetar o "Initial Value".
5. Adicione quantas variáveis precisar usando o botão **"Add"** para criar novas linhas de variáveis.

## Passo 4: Salvar e Utilizar o Ambiente

1. Clique no botão **"Add"** ou **"Save"** para salvar o ambiente.
2. Feche a janela **"Manage Environments"**.
3. Ao lado do ícone de engrenagem, no canto superior direito, haverá um dropdown onde você pode selecionar o ambiente que deseja ativar.
4. Selecione o ambiente criado. As variáveis desse ambiente estão agora disponíveis para uso nas suas requisições.

## Passo 5: Usar Variáveis nas Requisições

Para usar uma variável em uma requisição, insira o nome da variável entre chaves duplas, como `{{base_url}}`. O Postman substituirá automaticamente `{{base_url}}` pelo valor da variável do ambiente ativo quando você enviar a requisição.

# Configurar Script para Obtenção e Armazenamento do Token em Variável de Ambiente

Este tutorial descreve como configurar um script no Postman para capturar automaticamente um token de autenticação do corpo de uma resposta e salvar esse token em uma variável de ambiente.

### Passo 1: Enviar Requisição de Obtenção de Token

1. Crie ou selecione a requisição responsável por obter o token de autenticação.
2. Certifique-se de que a requisição está configurada corretamente e que o servidor responde com o token no corpo da resposta.

### Passo 2: Configurar o Script de Teste

1. Na requisição de obtenção do token, vá para a aba **"Tests"**.
2. Adicione o seguinte script:

```javascript
var jsonData = pm.response.json();
pm.environment.set("access_token", jsonData.access_token);
```

Este script extrai o `access_token` do corpo da resposta JSON e o salva em uma variável de ambiente chamada `access_token`.

### Passo 3: Salvar e Enviar a Requisição

1. Salve a requisição.
2. Envie a requisição e verifique se o token foi corretamente capturado e salvo na variável de ambiente.

## Adicionar a Variável de Ambiente nas Requests no Campo Authorization

Após configurar e armazenar o token de autenticação como uma variável de ambiente, você pode usá-lo em outras requisições para autenticação.

### Passo 1: Configurar o Cabeçalho de Autorização

1. Em qualquer requisição que requeira autenticação, vá para a aba **"Authorization"**.
2. No tipo de autenticação, selecione **"Bearer Token"**.
3. No campo do token, insira a variável de ambiente que contém o token no formato `{{access_token}}`.

### Passo 2: Enviar a Requisição

1. Envie a requisição.
2. O Postman substituirá automaticamente `{{access_token}}` pelo valor da variável de ambiente, autenticando a requisição.

Com esses passos, você pode automatizar o processo de autenticação em suas requisições, melhorando a eficiência dos testes no Postman.
