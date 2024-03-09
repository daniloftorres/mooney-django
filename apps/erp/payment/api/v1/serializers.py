from rest_framework import serializers
from apps.erp.payment.models import PaymentMethod


class PaymentMethodSerializer(serializers.ModelSerializer):

    class Meta:
        model = PaymentMethod
        fields = ('__all__')
