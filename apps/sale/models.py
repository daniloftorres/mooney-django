from django.conf import settings
from django.db import models
from django.utils import timezone
from apps.customer.models import Customer
from apps.core import models as models_base


class Sale(models_base.TimeStampedModel, models_base.SoftDeletionModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, verbose_name="Usuário")
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True, verbose_name="Cliente")
    date_time = models.DateTimeField(
        default=timezone.now, verbose_name="Data e Hora da Venda")
    total_price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Preço Total", default=0.00)

    def __str__(self):
        return f"Venda #{self.pk} - {self.date_time.strftime('%d/%m/%Y %H:%M')}"

    class Meta:
        verbose_name = "Venda"
        verbose_name_plural = "Vendas"


class SaleItem(models_base.TimeStampedModel, models_base.SoftDeletionModel):
    sale = models.ForeignKey(Sale, related_name='items',
                             on_delete=models.CASCADE, verbose_name="Venda")
    product = models.ForeignKey(
        'product.Product', on_delete=models.CASCADE, verbose_name="Produto")
    quantity = models.PositiveIntegerField(
        default=1, verbose_name="Quantidade")
    sale_price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Preço de Venda")

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"

    class Meta:
        verbose_name = "Item de Venda"
        verbose_name_plural = "Itens de Venda"


class PaymentMethod(models_base.TimeStampedModel, models_base.SoftDeletionModel):
    name = models.CharField(max_length=100, verbose_name="Nome")
    allows_installment = models.BooleanField(
        default=False, verbose_name="Permite Parcelamento")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Meio de Pagamento"
        verbose_name_plural = "Meios de Pagamento"


class SalePayment(models_base.TimeStampedModel, models_base.SoftDeletionModel):
    sale = models.OneToOneField(
        Sale, on_delete=models.CASCADE, related_name='payment', verbose_name="Venda")
    method = models.ForeignKey(
        PaymentMethod, on_delete=models.SET_NULL, null=True, verbose_name="Método de Pagamento")
    is_installment_payment = models.BooleanField(
        default=False, verbose_name="É Pagamento Parcelado?")
    total_installments = models.IntegerField(
        default=1, verbose_name="Total de Parcelas")
    total_paid = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Total Pago", default=0.00)

    def __str__(self):
        return f"Pagamento da Venda #{self.sale.pk}"

    class Meta:
        verbose_name = "Pagamento da Venda"
        verbose_name_plural = "Pagamentos das Vendas"


class SalePaymentInstallment(models_base.TimeStampedModel, models_base.SoftDeletionModel):
    sale_payment = models.ForeignKey(
        SalePayment, related_name='installments', on_delete=models.CASCADE, verbose_name="Pagamento da Venda")
    installment_number = models.IntegerField(verbose_name="Número da Parcela")
    due_date = models.DateField(verbose_name="Data de Vencimento")
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Valor da Parcela")
    paid = models.BooleanField(default=False, verbose_name="Pago")

    def __str__(self):
        return f"Parcela {self.installment_number} - Venda #{self.sale_payment.sale.pk}"

    class Meta:
        verbose_name = "Parcela do Pagamento"
        verbose_name_plural = "Parcelas dos Pagamentos"
        ordering = ['installment_number']
