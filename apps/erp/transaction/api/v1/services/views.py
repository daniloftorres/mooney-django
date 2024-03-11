from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .services import SaleTransactionService
from ..serializers import SaleTransactionSerializer


class SaleTransactionAPI(APIView):
    service_class = SaleTransactionService()

    def get(self, request, *args, **kwargs):

        sale_transaction = self.service_class.get_sale_transaction(**kwargs)
        serializer = SaleTransactionSerializer(sale_transaction)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        print("request.data :: ", request.data)
        serializer = SaleTransactionSerializer(data=request.data)
        if serializer.is_valid():
            if serializer.save():
                return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    """serializer = CustomerSerializer(data=request.data)
       if serializer.is_valid():
           if serializer.save():"""

    def put(self, request, *args, **kwargs):
        pass

    def delete(self, request, *args, **kwargs):
        pass


class SaleTransactionItemAPI(APIView):
    service = SaleTransactionService()

    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass

    def put(self, request, *args, **kwargs):
        pass

    def delete(self, request, *args, **kwargs):
        pass
