from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
import pytz
from apps.core import models as models_base

TIMEZONE_CHOICES = [
    ('UTC', _('Coordinated Universal Time')),
    ('EST', _('Eastern Standard Time')),
    ('CST', _('Central Standard Time')),
    ('MST', _('Mountain Standard Time')),
    ('PST', _('Pacific Standard Time')),
    # Adicione mais conforme necessário
]

LANGUAGE_CHOICES = [
    ('en', _('English')),
    ('pt-br', _('Portuguese (Brazil)')),
    # Adicione mais idiomas conforme necessário
]


class CustomUser(AbstractUser, models_base.TimeStampedModel, models_base.SoftDeletionModel):
    full_name = models.CharField(
        _('Full Name'), max_length=100, null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    # Adicione o campo de timezone
    # Usando pytz para gerar escolhas de timezone
    timezone = models.CharField(max_length=50, choices=[(
        tz, tz) for tz in pytz.all_timezones], default='UTC', verbose_name=_('Preferred Timezone'))
    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES,
                                default='en', verbose_name=_('Preferred Language'))

    class Meta:
        db_table = 'custom_user'
        verbose_name = _("Usuário")
        verbose_name_plural = _("Usuários")

    # Redefina os campos com related_name exclusivos
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="custom_user_groups",
        related_query_name="custom_user",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="custom_user_permissions",
        related_query_name="custom_user",
    )
