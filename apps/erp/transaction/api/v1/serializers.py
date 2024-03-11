from rest_framework import serializers
from apps.erp.transaction.models import Transaction, SaleTransaction, SaleTransactionItem, PaymentMethodSaleTransaction, PaymentInstallmentSaleTransaction
# from apps.sale.api.v1.serializers import SaleSerializer
from apps.account.models import CustomUser as User
from apps.customer.models import Customer


class PaymentMethodSaleTransaction(serializers.ModelSerializer):

    class Meta:
        model = PaymentMethodSaleTransaction
        fields = ('__all__')


class SaleTransactionItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = SaleTransactionItem
        fields = ('__all__')
        """extra_kwargs = {
            "sale_transaction": {'read_only': False, 'required': False}
        }"""


class PaymentInstallmentSaleTransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = PaymentInstallmentSaleTransaction
        fields = ('__all__')


class PaymentMethodSaleTransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = PaymentMethodSaleTransaction
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
    sale_date = serializers.DateTimeField(required=False, allow_null=True)

    items = SaleTransactionItemSerializer(required=False, many=True)
    payment_methods = PaymentMethodSaleTransactionSerializer(
        required=False, many=True)
    payment_installments = PaymentInstallmentSaleTransactionSerializer(
        required=False, allow_null=True, many=True)

    class Meta:
        model = SaleTransaction
        fields = ('__all__')

    def create(self, validated_data):
        print("init create ::: ", validated_data)
        items_data = validated_data.pop('items', [])
        payment_method_data = validated_data.pop('payment_methods', [])
        payment_installments = validated_data.pop('payment_installments', [])

        print("create ::: ", validated_data)
        sale_transaction = SaleTransaction.objects.create(**validated_data)
        print("sale_transaction ::: ", sale_transaction)
        print("sale_transaction.id ::: ", sale_transaction.id)

        if len(items_data) > 0:
            for item in items_data:
                SaleTransactionItem.objects.create(
                    sale_transaction=sale_transaction, **item)

        return sale_transaction


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = ('__all__')


"""class SaleTransactionSerializer(serializers.ModelSerializer):
    item = SaleTransactionItemSerializer(required=False, many=True)
    payment_method = PaymentMethodSaleTransactionSerializer(
        required=False, many=True)

    class Meta:
        fields = ('__all__')
        model = SaleTransaction"""
