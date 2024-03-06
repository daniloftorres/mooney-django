from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from apps.sale.models import Sale
# Importe o serializer apropriado
from apps.sale.api.v1.serializers import SaleSerializer


class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    permission_classes = [IsAuthenticated]
