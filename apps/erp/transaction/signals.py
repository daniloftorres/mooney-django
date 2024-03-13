from django.db.models.signals import pre_save, post_save, pre_delete
from django.dispatch import receiver
from .api.v1.services.services import SaleTransactionService
from .models import SaleTransactionItem


@receiver([post_save, pre_delete], sender=SaleTransactionItem)
def handle_change_in_sale_transaction_item(sender, instance, **kwargs):
    SaleTransactionService.handle_change_in_sale_transaction_item(instance)


@receiver(pre_save, sender=SaleTransactionItem)
def handle_before_save_sale_transaction_item(sender, instance, **kwargs):
    SaleTransactionService.handle_before_save_sale_transaction_item(instance)
