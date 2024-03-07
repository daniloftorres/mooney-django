from django.db import models
from django.utils.translation import gettext_lazy as _


class PaymentMethod(models.Model):
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
        return f"{self.get_payment_type_display()} - {self.description[:50]}"
