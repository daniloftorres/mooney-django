from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.core import models as models_base


class PaymentMethod(models_base.TimeStampedModel, models_base.SoftDeletionModel):
    # Payment types
    CASH = 'CSH'
    CHECK = 'CHK'
    CREDIT_CARD = 'CRC'
    DEBIT_CARD = 'DBT'
    BANK_TRANSFER = 'BKT'
    BOLETO = 'BLT'
    PIX = 'PIX'
    E_WALLET = 'EWT'

    PAYMENT_TYPE_CHOICES = [
        (CASH, _('Cash')),
        (CHECK, _('Check')),
        (CREDIT_CARD, _('Credit Card')),
        (DEBIT_CARD, _('Debit Card')),
        (BANK_TRANSFER, _('Bank Transfer')),
        (BOLETO, _('Boleto')),
        (PIX, _('PIX')),
        (E_WALLET, _('E-Wallet')),
    ]

    payment_type = models.CharField(
        max_length=3, choices=PAYMENT_TYPE_CHOICES, default=CASH, verbose_name=_('Payment Type'))
    description = models.CharField(max_length=255, blank=True, verbose_name=_(
        'Description'), help_text=_('Optional description of the payment method.'))

    def __str__(self):
        return f"{self.get_payment_type_display()} - {self.description[:50]}"

    class Meta:
        db_table = _("payment_method")
        verbose_name = _("Payment Method")
        verbose_name_plural = _("Payment Methods")
