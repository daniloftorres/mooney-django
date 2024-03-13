from django.db.models import Sum, F
from django.http import Http404
from apps.erp.transaction.models import SaleTransaction, SaleTransactionItem
# from apps.erp.transaction.api.v1.serializers import SaleTransactionSerializer


class SaleTransactionService:
    @staticmethod
    def get_sale_transaction_details(sale_transaction_id):

        try:
            return SaleTransaction.objects.get(id=sale_transaction_id)
        except SaleTransaction.DoesNotExist:
            raise Http404

    def create_sale_transaction(validated_data):
        # remove relationship
        items_data = validated_data.pop('items', [])
        payment_method_data = validated_data.pop('payment_methods', [])
        payment_installments = validated_data.pop('payment_installments', [])

        # create sala transaction
        sale_transaction = SaleTransaction.objects.create(**validated_data)

        # create items
        """if len(items_data) > 0:
            for item in items_data:
                SaleTransactionItem.objects.create(
                    sale_transaction=sale_transaction, **item)"""

        return sale_transaction

    def update_sale_transaction(instance, validated_data):

        # Atualiza campos diretos (não-relacionais)
        for field, value in validated_data.items():
            if field not in ['items', 'payment_methods', 'payment_installments']:
                setattr(instance, field, value)
        instance.save()

        # Atualiza itens da transação
        """if 'items' in validated_data:
            items_data = validated_data.pop('items')
            # Aqui você pode implementar a lógica para atualizar, criar ou excluir itens
            # Isso dependerá da sua lógica de negócios específica
            # Exemplo simples:
            instance.items.all().delete()  # Remover itens existentes e substituí-los
            for item_data in items_data:
                SaleTransactionItem.objects.create(
                    sale_transaction=instance, **item_data)"""

        return instance

    @staticmethod
    def update_sale_transaction_totals(sale_transaction_id):
        sale_transaction = SaleTransaction.objects.get(id=sale_transaction_id)
        items = SaleTransactionItem.objects.filter(
            sale_transaction_id=sale_transaction_id)

        total_quantity = items.aggregate(
            total=Sum(F('quantity')))['total'] or 0
        total_amount = items.aggregate(total=Sum(
            F('quantity') * F('sale_price') * (1 - F('discount') / 100)))['total'] or 0
        total_discount_amount = items.aggregate(
            total=Sum(F('quantity') * F('sale_price') * F('discount') / 100))['total'] or 0

        sale_transaction.total_quantity = total_quantity
        sale_transaction.total_amount = total_amount
        sale_transaction.total_discount_amount = total_discount_amount
        sale_transaction.net_amount = total_amount - total_discount_amount
        sale_transaction.save()

    @staticmethod
    def handle_change_in_sale_transaction_item(instance):
        SaleTransactionService.update_sale_transaction_totals(
            instance.sale_transaction.id)

    @staticmethod
    def handle_before_save_sale_transaction_item(instance):
        if instance.pk:
            original_item = SaleTransactionItem.objects.get(pk=instance.pk)
            if instance.quantity != original_item.quantity or instance.sale_price != original_item.sale_price or instance.discount != original_item.discount:
                instance.total_amount = instance.quantity * \
                    instance.sale_price * (1 - instance.discount / 100)
                SaleTransactionService.update_sale_transaction_totals(
                    instance.sale_transaction.id)
        else:
            instance.total_amount = instance.quantity * \
                instance.sale_price * (1 - instance.discount / 100)


class SaleTransactionItemService:

    @staticmethod
    def get_sale_transiction_item(sale_transaction_item_id):
        try:
            return SaleTransactionItem.objects.get(id=sale_transaction_item_id)
        except SaleTransactionItem.DoesNotExist:
            raise Http404

    def create_sale_transaction_item(validated_data):
        return SaleTransactionItem.objects.create(**validated_data)

    def update_sale_transaction_item(instance, validated_data):
        print("##update_sale_transaction_item validated_data  ", validated_data)
        return SaleTransactionItem.objects.filter(id=instance.id).update(**validated_data)

    def remove_sale_transaction_item(sale_transaction_item_id):
        pass
