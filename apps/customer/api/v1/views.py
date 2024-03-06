from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from apps.customer.models import Customer  # Importe seu modelo Customer
# Importe o serializer apropriado
from apps.customer.api.v1.serializers import CustomerSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]
