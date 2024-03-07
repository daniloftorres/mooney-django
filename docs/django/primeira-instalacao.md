## Primeira Instalação e Configuração do Django

1. Instalação no ambiente local usando o PIP:

   ```bash
   pip install Django==3.2.5
   ```

2. Iniciando o Projeto Localmente

   ```bash
      django-admin startproject mooney .
   ```

3. Criando o Primeiro APP

   ```bash
      mkdir -p ./apps/erp/lancamento
      python manage.py startapp lancamento ./apps/erp/lancamento
      sudo chown -R danilo:danilo ./apps/erp/pagamento

      mkdir -p ./apps/erp/transaction
      python manage.py startapp transaction ./apps/erp/transaction
      sudo chown -R danilo:danilo ./apps/erp/transaction

   ```

   ```bash
       django-admin startapp account apps/account
   ```
