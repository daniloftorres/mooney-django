from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.core import models as models_base
from apps.erp.payment.models import PaymentMethod

STATUS_TRANSACTION = (
    ('Pending', _('Pending')),
    ('Paid', _('Paid')),
    ('Cancelled', _('Cancelled')),
)

TYPE_TRANSACTION = (
    ('sale', _('Sale')),
)


"""SALE_TRANSACTION_STATUS = (
    ('Pending', _('Pending')),
    ('Paid', _('Paid')),
    ('Cancelled', _('Cancelled')),
)"""

SALE_TRANSACTION_TYPE = (
    ('expense', _('Expense')),
    ('revenue', _('Revenue')),
)

PAYMENT_INSTALLMENT_TRANSACTION_TYPE = (
    ('Pending', _('Pending')),
    ('Paid', _('Paid')),
    ('Cancelled', _('Cancelled')),
)

STATUS_TRANSACTION_SALE = (
    ('creation', _('Order Creation')),
    ('billing', _('Billing')),
    ('payment_pending', _('Payment Pending')),
    ('payment_processing', _('Payment Processing')),
    ('payment_approved', _('Payment Approved')),
    ('payment_denied', _('Payment Denied')),
    ('cancelled', _('Cancelled')),
    ('returned', _('Returned')),
    ('refunded', _('Refunded')),
)


class Transaction(models_base.TimeStampedModel, models_base.SoftDeletionModel):
    status = models.CharField(max_length=20, choices=STATUS_TRANSACTION,
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


class SaleTransaction(models_base.TimeStampedModel, models_base.SoftDeletionModel):
    sale_transaction_status = models.CharField(
        max_length=20, choices=STATUS_TRANSACTION_SALE, default='creation', verbose_name=_("Status"))
    sale_transaction_type = models.CharField(
        max_length=10, choices=SALE_TRANSACTION_TYPE, default='expense', verbose_name=_("Sale Transaction Type"))
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, verbose_name=_("User"))
    customer = models.ForeignKey(
        'customer.Customer', on_delete=models.CASCADE, verbose_name=_('Customer'), null=True, default=None)
    seller = models.ForeignKey(
        'account.CustomUser', on_delete=models.CASCADE, verbose_name=_('Seller'), null=True, default=None, related_name="sale_transaction_seller")
    total_amount = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name=_('Total Amount'), null=True)
    total_discount_amount = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name=_('Total Discount Amount'), null=True)
    net_amount = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name=_('Net Amount'), null=True)
    tax_amount = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name=_('Tax Amount'), null=True)
    sale_date = models.DateTimeField(verbose_name=_('Sale Date'), null=True)

    class Meta:
        db_table = _("transaction_sale")
        verbose_name = _("Sale Transaction")
        verbose_name_plural = _("Sales Transactions")


class SaleTransactionItem(models_base.TimeStampedModel, models_base.SoftDeletionModel):
    sale_transaction = models.ForeignKey(SaleTransaction, related_name='items',
                                         on_delete=models.CASCADE, verbose_name=_("Sale"))
    product = models.ForeignKey(
        'product.Product', on_delete=models.CASCADE, verbose_name=_("Product"))
    quantity = models.PositiveIntegerField(
        default=1, verbose_name=_("Quantity"))
    sale_price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name=_("Sale Price"), null=True)

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"

    class Meta:
        db_table = 'sale_item'
        verbose_name = _("Sale Item")
        verbose_name_plural = _("Sale Items")


class PaymentMethodSaleTransaction(models.Model):

    payment_method = models.ForeignKey(
        PaymentMethod, on_delete=models.CASCADE, verbose_name=_(''), null=True)

    sale_transaction = models.ForeignKey(
        SaleTransaction, on_delete=models.CASCADE, verbose_name=_(''), null=True, related_name="payment_methods")

    payment_date = models.DateTimeField(auto_now_add=True, verbose_name=_(
        'Payment Date'), help_text=_('Date and time the payment was registered.'))

    # Specific fields for methods that require it
    issuing_bank = models.CharField(max_length=50, blank=True, verbose_name=_(
        'Issuing Bank'), help_text=_('Issuing bank for checks or bank transfers.'))
    number = models.CharField(max_length=20, blank=True, verbose_name=_(
        'Number'), help_text=_('Check or card number.'))
    validity = models.DateField(blank=True, null=True, verbose_name=_(
        'Validity'), help_text=_('Card validity date, if applicable.'))
    payer_cpf_cnpj = models.CharField(max_length=14, blank=True, verbose_name=_(
        'Payer CPF/CNPJ'), help_text=_('Payer’s CPF or CNPJ for PIX or boletos.'))
    pix_key = models.CharField(max_length=255, blank=True, verbose_name=_(
        'PIX Key'), help_text=_('PIX key for payments via PIX.'))
    e_wallet_provider = models.CharField(max_length=50, blank=True, verbose_name=_(
        'E-Wallet Provider'), help_text=_('Provider of the E-Wallet, if applicable.'))

    def __str__(self):
        return f"{self.payment_method.get_payment_type_display()} - {self.payment_method.description[:50]}"


class PaymentInstallmentSaleTransaction(models.Model):
    sale_transaction = models.ForeignKey(
        SaleTransaction, on_delete=models.CASCADE, verbose_name=_('Sale Transaction'), null=True, related_name='payment_installments')
    status = models.CharField(
        max_length=10, choices=PAYMENT_INSTALLMENT_TRANSACTION_TYPE, default='Pending', verbose_name=_('Status'))
    payment_method = models.ForeignKey(
        'payment.PaymentMethod', on_delete=models.CASCADE, verbose_name=_('Payment Method'), null=True)
    # installment = models.IntegerField(verbose_name=_('Installment Number'))
    installment = models.PositiveIntegerField(blank=True, verbose_name=_(
        'Installment Number'), null=True)
    total_amount = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name=_("Total Amount"), null=True)
    total_discount_amount = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name=_('Total Discount Amount'), null=True)
    net_amount = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name=_("Net Amount"), null=True)
    tax_amount = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name=_('Tax Amount'), null=True)
    notes = models.TextField(blank=True, verbose_name=_('Notes'))

    class Meta:
        db_table = _("transaction_payment_installment")
        verbose_name = _("Payment of Transaction Installments")
        verbose_name_plural = _("Payments of Transaction Installments")
