from django.conf import settings
from django.db import models
from django.utils import timezone
from apps.customer.models import Customer
from apps.core import models as models_base
from django.utils.translation import gettext_lazy as _
from apps.erp.payment.models import PaymentMethod

STATUS_SALE = (
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


class Sale(models_base.TimeStampedModel, models_base.SoftDeletionModel):
    status = models.CharField(
        max_length=20, choices=STATUS_SALE, default='creation', verbose_name=_("Status"))
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, verbose_name=_("User"))
    seller = models.ForeignKey('account.CustomUser',
                               on_delete=models.CASCADE, related_name='sales', verbose_name=_("Seller"), blank=True, null=True)
    payment_method = models.ForeignKey(
        PaymentMethod, on_delete=models.CASCADE, null=True, verbose_name=_("Payment Method"))
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True, verbose_name=_("Customer"))
    date_time = models.DateTimeField(
        default=timezone.now, verbose_name=_("Sale Date and Time"))
    total_price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name=_("Total Price"), default=0.00)

    def __str__(self):
        return f"Sale #{self.pk} - {self.date_time.strftime('%d/%m/%Y %H:%M')}"

    class Meta:
        db_table = 'sale'
        verbose_name = _("Sale")
        verbose_name_plural = _("Sales")


class SaleItem(models_base.TimeStampedModel, models_base.SoftDeletionModel):
    sale = models.ForeignKey(Sale, related_name='items',
                             on_delete=models.CASCADE, verbose_name=_("Sale"))
    product = models.ForeignKey(
        'product.Product', on_delete=models.CASCADE, verbose_name=_("Product"))
    quantity = models.PositiveIntegerField(
        default=1, verbose_name=_("Quantity"))
    sale_price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name=_("Sale Price"))

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"

    class Meta:
        db_table = 'sale_item'
        verbose_name = _("Sale Item")
        verbose_name_plural = _("Sale Items")
