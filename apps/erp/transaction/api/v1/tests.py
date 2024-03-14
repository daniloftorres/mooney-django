from django.test import TestCase
from django.utils import timezone
from apps.erp.transaction.models import SaleTransaction, SaleTransactionItem
from apps.account.models import CustomUser as User
from apps.customer.models import Customer
from apps.product.models import Product


class SaleTransactionTest(TestCase):

    def setUp(self):
        # Criando o usuário
        self.user = User.objects.create_user(
            username='testuser', password='12345')

        # Criando o cliente
        self.customer = Customer.objects.create(
            name="Test Customer", email="customer@test.com")

        # Criando o vendedor
        self.seller = User.objects.create_user(
            username='testseller', password='12345')

        # Criando o produto
        self.product = Product.objects.create(
            name="Test Product", price=100.00)

        # Criando a transação de venda
        self.sale_transaction = SaleTransaction.objects.create(
            user=self.user,
            customer=self.customer,
            seller=self.seller,
            total_quantity=1,
            total_amount=100.00,
            total_discount_amount=0.00,
            net_amount=100.00,
            tax_amount=0.00,
            sale_date=timezone.now()
        )

        # Criando um item da transação de venda
        self.sale_transaction_item = SaleTransactionItem.objects.create(
            sale_transaction=self.sale_transaction,
            product=self.product,
            quantity=1,
            sale_price=100.00,
            total_amount=100.00,
            discount=0.00
        )

    def test_sale_transaction_creation(self):
        self.assertEqual(self.sale_transaction.total_amount, 100.00)
        self.assertEqual(self.sale_transaction.net_amount, 100.00)
        self.assertEqual(
            self.sale_transaction.sale_transaction_status, 'creation')
        self.assertEqual(self.sale_transaction_item.product, self.product)
        self.assertEqual(self.sale_transaction_item.quantity, 1)
        self.assertEqual(self.sale_transaction.items.count(), 1)
