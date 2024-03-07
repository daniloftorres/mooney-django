from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.core import models as models_base

STATUS_TRANSACTION = (
    ('Pending', _('Pending')),
    ('Paid', _('Paid')),
    ('Cancelled', _('Cancelled')),
)

TYPE_TRANSACTION = (
    ('sale', _('Sale')),
)

SALE_TRANSACTION_STATUS = (
    ('Pending', _('Pending')),
    ('Paid', _('Paid')),
    ('Cancelled', _('Cancelled')),
)

SALE_TRANSACTION_TYPE = (
    ('expense', _('Expense')),
    ('revenue', _('Revenue')),
)

PAYMENT_INSTALLMENT_TRANSACTION_TYPE = (
    ('Pending', _('Pending')),
    ('Paid', _('Paid')),
    ('Cancelled', _('Cancelled')),
)


class Transaction(models_base.TimeStampedModel, models_base.SoftDeletionModel):
    status = models.CharField(max_length=10, choices=STATUS_TRANSACTION,
                              default='Pending', verbose_name=_('Transaction Status'))
    type_transaction = models.CharField(
        max_length=4, choices=TYPE_TRANSACTION, verbose_name=_('Transaction Type'))
    total_amount = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name=_('Total Amount'))
    total_discount_amount = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name=_('Total Discount Amount'))
    net_amount = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name=_('Net Amount'))
    notes = models.TextField(blank=True, verbose_name=_('Notes'))

    class Meta:
        db_table = "transaction"
        verbose_name = _("Transaction")
        verbose_name_plural = _("Transactions")


class SaleTransaction(Transaction):
    sale_transaction_status = models.CharField(
        max_length=10, choices=SALE_TRANSACTION_STATUS, default='Pending', verbose_name=_('Sale Transaction Status'))
    sale_transaction_type = models.CharField(
        max_length=10, choices=SALE_TRANSACTION_TYPE, verbose_name=_("Sale Transaction Type"))
    payment_type = models.ForeignKey(
        'payment.PaymentMethod', on_delete=models.CASCADE, verbose_name=_('Payment Type'))
    customer = models.ForeignKey(
        'customer.Customer', on_delete=models.CASCADE, verbose_name=_('Customer'))
    seller = models.ForeignKey(
        'account.CustomUser', on_delete=models.CASCADE, verbose_name=_('Seller'))
    sale = models.ForeignKey(
        'sale.Sale', on_delete=models.CASCADE, verbose_name=_('Sale'))
    tax_amount = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name=_('Tax Amount'))
    sale_date = models.DateTimeField(verbose_name=_('Sale Date'))

    class Meta:
        db_table = _("transaction_sale")
        verbose_name = _("Sale Transaction")
        verbose_name_plural = _("Sales Transactions")


class PaymentInstallmentTransaction(models.Model):
    sale_transaction = models.ForeignKey(
        SaleTransaction, on_delete=models.CASCADE, verbose_name=_('Sale Transaction'))
    status = models.CharField(
        max_length=10, choices=PAYMENT_INSTALLMENT_TRANSACTION_TYPE, verbose_name=_('Status'))
    payment_method = models.ForeignKey(
        'payment.PaymentMethod', on_delete=models.CASCADE, verbose_name=_('Payment Method'))
    installment = models.IntegerField(verbose_name=_('Installment Number'))
    total_amount = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name=_("Total Amount"))
    total_discount_amount = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name=_('Total Discount Amount'))
    net_amount = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name=_("Net Amount"))
    tax_amount = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name=_('Tax Amount'))
    notes = models.TextField(blank=True, verbose_name=_('Notes'))

    class Meta:
        db_table = _("transaction_payment_installment")
        verbose_name = _("Payment of Transaction Installments")
        verbose_name_plural = _("Payments of Transaction Installments")
