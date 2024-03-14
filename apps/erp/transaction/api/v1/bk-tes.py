from django.test import TestCase
from django.utils import timezone
# Ajuste o import conforme o caminho correto do seu modelo
from apps.erp.transaction.models import Transaction
# Supondo que você tenha um modelo Customer para usar nos testes
from apps.customer.models import Customer
# Supondo que você tenha um modelo PaymentMethod para usar nos testes
from apps.erp.payment.models import PaymentMethod
# Supondo que você tenha um modelo CustomUser para usar nos testes
from apps.account.models import CustomUser
# Supondo que você tenha um modelo Sale para usar nos testes
from apps.sale.models import Sale


class TransactionModelTest(TestCase):

    def setUp(self):
        # Setup run before every test method.
        self.customer = Customer.objects.create(
            name="Test Customer", email="test@example.com", phone="1234567890")
        self.payment_method = PaymentMethod.objects.create(
            payment_type="CSH")
        self.seller = CustomUser.objects.create_user(
            username="seller", password="test")
        self.sale = Sale.objects.create(
            customer=self.customer, total_price=100.00, date_time=timezone.now(), user_id=1)
        self.transaction = Transaction.objects.create(
            type_transaction='sale',
            total_amount=100.00,
            total_discount_amount=10.00,
            net_amount=90.00,
            notes="Test transaction"
        )

    def test_transaction_creation(self):
        # Test the transaction instance
        self.assertTrue(isinstance(self.transaction, Transaction))
        self.assertEqual(self.transaction.total_amount, 100.00)
        self.assertEqual(self.transaction.total_discount_amount, 10.00)
        self.assertEqual(self.transaction.net_amount, 90.00)
        self.assertEqual(self.transaction.notes, "Test transaction")

# Você pode adicionar mais métodos de teste conforme necessário para testar outros aspectos do modelo Transaction.
