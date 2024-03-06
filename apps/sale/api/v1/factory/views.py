from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.sale.api.v1.factory.factory import BasicSaleFactory
from apps.customer.models import Customer


class SaleEntryView (APIView):
    def post(self, request, *args, **kwargs):
        factory = BasicSaleFactory()
        print("check user", request.user)
        customer_id = request.data.get('customer_id')
        customer = Customer.objects.get(id=customer_id)
        sale = factory.create_sale(
            user=request.user,
            customer=customer,
            items=request.data.get('items')
        )

        return Response({
            'message': "Venda criada com sucesso!",
            'sale_id': sale.id
        }, status=status.HTTP_201_CREATED)
