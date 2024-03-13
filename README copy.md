# Project Mooney | API

# Índice

- [Teoria Geral](docs/teoria.md)

## Instando e Configurando Todo o Ambiente

- [Ambiente Usado](docs/ambientes.md)
- [Pré-requisitos](docs/pre-requisitos.md)
- [Django](docs/django.md)

### Modulo Usuário

1. [Usuário](docs/django/usuario/usuario.md)

   - Fluxo de Api RestFull (Django Rest Framework DRF)
     - Get, Post, Put, Path e Delete
   - Autenticação
     - JWT e OAuth2
   - Test:
     - Teste unitario para JWT e OAuth2
   - Designer Parttners MV (sem o T)

### Modulo Cliente

1. [Cliente](docs/django/cliente/cliente.md)

   - Fluxo de Api RestFull (Django Rest Framework DRF)

### Modulo Produto

1. [Produto](docs/django/produto/produto.md)

   - Categoria
   - Imagem

### Modulo Venda

1. [Venda](docs/django/venda/venda.md)

   Função: Calcula Total Venda (Selecionar todos os items, pegar valor e desconto e realizar os calculos e salvar na tabela principal SaleTransaction)

   Função: Calcula Total a Ser Pago Conforme Forma de Pagamento :

   - Cria registro no PaymentInstallmentSaleTransaction conforme, quantidade de parcelas ou apenas 1 para avista

   Action : Nova Venda

   - Cria SaleTransaction com status : creating
   - Calcula Total Venda

   Action : Adicionar Item

   - Criar registro no SaleTransactionItem relacionado com o id do SaleTransaction
   - Calcula Total Venda

   Action : Atualizar Item

   - Atuzaliar registro no SaleTransactionItem relacionado com o id do SaleTransactionItem
   - Calcula Total Venda

   Action : Remove Item

   - Remove registro no SaleTransactionItem relacionado com o id do SaleTransactionItem
   - Calcula Total Venda

   Action : Forma de pagamento

   - action : Adicionar Forma de Pagamento

     - Adicionar Registro da Forma escolhida em : PaymentMethodSaleTransaction

   - action : Remover Forma de Pagamento
     - Remover Registro da Forma escolhida em : PaymentMethodSaleTransaction

   Sale : creating
   -> items

### Modulo Financeiro

1. [Financeiro](docs/django/financeiro/financeiro.md)

   - Lançamentos
   - Forma de Pagamento
   - Lançamento Parcela

   App : Financeiro

   SALE_TRANSACTION_TYPES = (
   ('expense', 'Expense'),
   ('revenue', 'Revenue'),
   )

   TRANSACTION_TYPES = (
   ('sale', 'Sale'),
   )

   Transaction

   - id
   - status
   - transaction_type
   - total_amount
   - total_discount_amount
   - net_amount
   - notes

   SaleTransaction(Transaction)

   - sale_transaction_status
   - sale_transaction_type
   - payment_type_id
   - customer_id
   - seller_id
   - sale_id
   - tax_amount
   - sale_date

   PaymentInstallmentTransaction

   - id
   - sale_transaction_id (N:1)
   - status : (Pending, Paid, Cancelled)
   - payment_method_id
   - installment
   - total_amount
   - total_discount_amount
   - net_amount
   - tax_amount
   - notes
