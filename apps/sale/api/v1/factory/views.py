from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.sale.api.v1.factory.factory import BasicSaleFactory
from apps.erp.transaction.models import SaleTransaction
from apps.customer.models import Customer
from apps.erp.transaction.api.v1.serializers import SaleTransactionSerializer


class SaleEntryView (APIView):

    def get_object(self, pk):
        try:
            return SaleTransaction.objects.get(pk=pk)
        except SaleTransaction.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):

        sale = self.get_object(pk)
        sale = SaleSerializer(sale)
        return Response(sale.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        factory = BasicSaleFactory()
        customer = request.data.get('customer')
        customer = Customer.objects.get(id=customer)
        sale = factory.create_sale(
            user=request.user,
            customer=customer,
            items=request.data.get('items')
        )

        return Response({
            'message': "Venda criada com sucesso!",
            'sale_id': sale.id
        }, status=status.HTTP_201_CREATED)

    def put(self, request, pk):
        sale = self.get_object(pk)
        sale = SaleSerializer(sale, data=request.data)
        if sale.is_valid():
            sale.save()
            return Response(sale.data, status=status.HTTP_200_OK)
        return Response(sale.errors, status=status.HTTP_400_BAD_REQUEST)
