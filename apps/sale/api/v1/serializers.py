from rest_framework import serializers
from apps.sale.models import Sale


class SaleSerializer (serializers.ModelSerializer):

    class Meta:
        model = Sale
        fields = '__all__'
