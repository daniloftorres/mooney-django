from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404
from .services import SaleTransactionService, SaleTransactionItemService, SaleTransactionPaymentMethodService, PaymentExceededException
from ..serializers import SaleTransactionSerializer, SaleTransactionItemSerializer, SaleTransactionPaymentMethodSerializer
from ....models import SaleTransaction, SaleTransactionItem, SaleTransactionPaymentMethod


class SaleTransactionServiceAPI(APIView):
    service_class = SaleTransactionService()

    def get_object(self, pk):
        try:
            return SaleTransaction.objects.get(id=pk)
        except SaleTransaction.DoesNotExist:
            raise Http404

    def get(self, request, pk, *args, **kwargs):
        sale_transaction = SaleTransactionService.get_sale_transaction_details(
            pk)
        return Response(SaleTransactionSerializer(sale_transaction).data, status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = SaleTransactionSerializer(data=request.data)
        if serializer.is_valid():
            sale_transaction = SaleTransactionService.create_sale_transaction(
                serializer.validated_data)
            return Response(SaleTransactionSerializer(sale_transaction).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, *args, **kwargs):
        object = self.get_object(pk)
        serializer = SaleTransactionSerializer(object, data=request.data)
        if serializer.is_valid():
            sale_transaction = SaleTransactionService.update_sale_transaction(object,
                                                                              serializer.validated_data)
            return Response(SaleTransactionSerializer(sale_transaction).data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, * args, **kwargs):
        sale_transaction = self.get_object(pk)
        sale_transaction.delete()
        sale_transaction.save()
        return Response(status.HTTP_204_NO_CONTENT)


class SaleTransactionItemServiceAPI(APIView):
    service = SaleTransactionItemService

    def get_object(self, pk):
        try:
            return SaleTransactionItem.objects.get(id=pk)
        except SaleTransactionItem.DoesNotExist:
            raise Http404

    def get(self, request, pk, *args, **kwargs):

        sale_transaction_item = self.service.get_sale_transiction_item(
            pk)
        serializer = SaleTransactionItemSerializer(sale_transaction_item)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = SaleTransactionItemSerializer(data=request.data)
        if serializer.is_valid():
            sale_transaction_item = self.service.create_sale_transaction_item(
                serializer.validated_data)
            if sale_transaction_item:
                return Response(SaleTransactionItemSerializer(sale_transaction_item).data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, *args, **kwargs):
        object = self.get_object(pk)
        serializer = SaleTransactionItemSerializer(object, data=request.data)
        if serializer.is_valid():
            sale_transaction_item = self.service.update_sale_transaction_item(
                object, serializer.validated_data)
            if sale_transaction_item:
                sale_transaction_item = self.service.get_sale_transiction_item(
                    pk)
                return Response(SaleTransactionItemSerializer(sale_transaction_item).data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        sale_transaction_item = self.get_object(pk)
        sale_transaction_item.delete()
        return Response(status.HTTP_204_NO_CONTENT)


class SaleTransactionPaymentMethodServiceAPI(APIView):
    service = SaleTransactionPaymentMethodService

    def get_object(self, pk):
        try:
            return SaleTransactionPaymentMethod.objects.get(id=pk)
        except SaleTransactionPaymentMethod.DoesNotExist:
            raise Http404

    def get(self, request, pk, *args, **kwargs):

        sale_transaction_payment_method = self.service.get_sale_transiction_payment_method(
            pk)
        serializer = SaleTransactionPaymentMethodSerializer(
            sale_transaction_payment_method)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = SaleTransactionPaymentMethodSerializer(data=request.data)
        if serializer.is_valid():
            try:
                sale_transaction_payment_method = self.service.create_sale_transaction_payment_method(
                    serializer.validated_data)
                return Response(SaleTransactionPaymentMethodSerializer(sale_transaction_payment_method).data, status.HTTP_201_CREATED)
            except PaymentExceededException as e:
                return Response({"error": str(e)}, status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, *args, **kwargs):
        object = self.get_object(pk)
        serializer = SaleTransactionPaymentMethodSerializer(
            object, data=request.data)
        if serializer.is_valid():
            sale_transaction_payment_method = self.service.update_sale_transaction_payment_method(
                object, serializer.validated_data, pk)
            if sale_transaction_payment_method:
                sale_transaction_payment_method = self.service.get_sale_transiction_payment_method(
                    pk)
                return Response(SaleTransactionPaymentMethodSerializer(sale_transaction_payment_method).data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        sale_transaction_payment_method = self.get_object(pk)
        sale_transaction_payment_method.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
