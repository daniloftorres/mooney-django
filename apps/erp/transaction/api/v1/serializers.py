from rest_framework import serializers
from apps.erp.transaction.models import Transaction, SaleTransaction, SaleTransactionItem, SaleTransactionPaymentInstallment, SaleTransactionPaymentMethod
# from apps.sale.api.v1.serializers import SaleSerializer
from apps.account.models import CustomUser as User
from apps.customer.models import Customer
from apps.product.models import Product


class PaymentMethodSaleTransaction(serializers.ModelSerializer):

    class Meta:
        model = SaleTransactionPaymentMethod
        fields = ('__all__')


class SaleTransactionItemSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all())

    class Meta:
        model = SaleTransactionItem
        fields = ('__all__')
        extra_kwargs = {
            "sale_transaction": {'read_only': False, 'required': False}
        }

    def create(self, validate_data):
        print("into create")
        sale_trasaction_item = SaleTransactionItem.objects.create(
            **validate_data)
        print('apos create item', sale_trasaction_item)
        return sale_trasaction_item


class SaleTransactionPaymentInstallmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = SaleTransactionPaymentInstallment
        fields = ('__all__')


class SaleTransactionPaymentMethodSerializer(serializers.ModelSerializer):

    class Meta:
        model = SaleTransactionPaymentMethod
        fields = ('__all__')


class SaleTransactionSerializer(serializers.ModelSerializer):
    customer = serializers.PrimaryKeyRelatedField(
        queryset=Customer.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    seller = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    total_amount = serializers.DecimalField(
        required=False, allow_null=True, max_digits=10, decimal_places=2)
    net_amount = serializers.DecimalField(
        required=False, allow_null=True, max_digits=10, decimal_places=2)
    total_discount_amount = serializers.DecimalField(
        required=False, allow_null=True, max_digits=10, decimal_places=2)
    tax_amount = serializers.DecimalField(
        required=False, allow_null=True, max_digits=10, decimal_places=2)
    total_due = serializers.DecimalField(
        required=False, allow_null=True, max_digits=10, decimal_places=2)
    sale_date = serializers.DateTimeField(required=False, allow_null=True)

    items = SaleTransactionItemSerializer(required=False, many=True)
    payment_methods = SaleTransactionPaymentMethodSerializer(
        required=False, many=True)
    payment_installments = SaleTransactionPaymentInstallmentSerializer(
        required=False, allow_null=True, many=True)

    class Meta:
        model = SaleTransaction
        fields = ('__all__')

    def create(self, validated_data):

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

    def update(self, instance, validated_data):

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

        # Similar para payment_methods e payment_installments
        # Implemente a lógica conforme necessário para seu modelo de dados e regras de negócio

        return instance


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = ('__all__')
