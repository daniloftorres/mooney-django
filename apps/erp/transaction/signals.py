from django.db.models.signals import pre_save, post_save, pre_delete
from django.dispatch import receiver
from django.db.models import Sum, F

from .models import SaleTransactionItem, SaleTransaction

# Função para recalcular e atualizar o total do SaleTransaction
print("atualizando via signal INIT INIT")


def update_sale_transaction_totals(sale_transaction_id):
    print("atualizando via signal")
    sale_transaction = SaleTransaction.objects.get(id=sale_transaction_id)
    items = SaleTransactionItem.objects.filter(
        sale_transaction_id=sale_transaction_id)

    total_amount = items.aggregate(
        total=Sum(F('quantity') * F('sale_price')))['total'] or 0
    total_discount_amount = items.aggregate(
        total=Sum('discount'))['total'] or 0

    # Aqui você pode adicionar a lógica para calcular a média dos descontos se necessário
    # Isso é um pouco mais complexo porque depende exatamente de como você quer tratar diferentes descontos
    # Para simplificar, estou apenas somando os descontos

    sale_transaction.total_amount = total_amount
    sale_transaction.total_discount_amount = total_discount_amount
    sale_transaction.net_amount = total_amount - total_discount_amount
    sale_transaction.save()

# Sinal para atualizar os totais quando um SaleTransactionItem é criado ou atualizado


@receiver([post_save, pre_delete], sender=SaleTransactionItem)
def handle_change_in_sale_transaction_item(sender, instance, **kwargs):
    print("atualizando via signal")
    update_sale_transaction_totals(instance.sale_transaction.id)

# Opcionalmente, você pode querer lidar com a atualização antes de salvar para realizar cálculos baseados em mudanças


@receiver(pre_save, sender=SaleTransactionItem)
def handle_before_save_sale_transaction_item(sender, instance, **kwargs):
    print("atualizando via signal")
    if instance.pk:  # Se o item já existir, verifique se houve mudanças relevantes antes de prosseguir
        original_item = SaleTransactionItem.objects.get(pk=instance.pk)
        if instance.quantity != original_item.quantity or instance.sale_price != original_item.sale_price:
            update_sale_transaction_totals(instance.sale_transaction.id)
