from rest_framework import serializers
from apps.erp.transaction.models import Transaction, SaleTransaction, PaymentMethodSaleTransaction, PaymentInstallmentSaleTransaction
# from apps.sale.api.v1.serializers import SaleSerializer


class SaleTransactionSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('__all__')
        model = SaleTransaction


class PaymentInstallmentSaleTransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = PaymentInstallmentSaleTransaction
        fields = ('__all__')


class PaymentMethodSaleTransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = PaymentMethodSaleTransaction
        fields = ('__all__')


class SaleTransactionSerialize(serializers.ModelSerializer):
    customer = serializers.StringRelatedField()
    user = serializers.StringRelatedField()
    seller = serializers.StringRelatedField()
    payment_method = PaymentMethodSaleTransactionSerializer()
    payment_installment = PaymentInstallmentSaleTransactionSerializer()

    class Meta:
        model = SaleTransaction
        fields = ('__all__')


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = ('__all__')
