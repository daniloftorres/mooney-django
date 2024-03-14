from django.test import TestCase
from django.utils import timezone
from apps.erp.transaction.models import Transaction
from apps.customer.models import Customer
from apps.erp.payment.models import PaymentMethod
from apps.account.models import CustomUser
from apps.sale.models import Sale


class TransactionModelTest(TestCase):

    def setUp(self):
        self.customer = Customer.objects.create(
            nome="Test Customer", email="test@example.com", telefone="1234567890")
        self.payment_method = PaymentMethod.objects.create(
            name="Test Payment Method")
        self.seller = CustomUser.objects.create_user(
            username="seller", password="test")
        self.sale = SaleTransa.objects.create(
            customer=self.customer, total_price=100.00, sale_date=timezone.now())
        self.transaction = Transaction.objects.create(
            type_transaction='sale',
            total_amount=100.00,
            total_discount_amount=10.00,
            net_amount=90.00,
            notes="Test transaction"
        )

    def test_transaction_creation(self):
        self.assertTrue(isinstance(self.transaction, Transaction))
        self.assertEqual(self.transaction.total_amount, 100.00)
        self.assertEqual(self.transaction.total_discount_amount, 10.00)
        self.assertEqual(self.transaction.net_amount, 90.00)
        self.assertEqual(self.transaction.notes, "Test transaction")
