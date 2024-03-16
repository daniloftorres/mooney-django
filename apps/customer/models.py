from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.core import models as models_base


class Customer(models_base.TimeStampedModel, models_base.SoftDeletionModel):
    name = models.CharField(max_length=100, verbose_name=_(
        "Name"), blank=True, null=True)
    email = models.EmailField(verbose_name=_("Email"), blank=True, null=True)
    phone = models.CharField(
        max_length=15, verbose_name=_("Phone"), blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Customer')
        verbose_name_plural = _('Customers')
        db_table = 'customer'
