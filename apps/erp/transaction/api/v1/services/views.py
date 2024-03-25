from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from apps.erp.transaction.api.v1.services.services import (
    SaleTransactionService,
    SaleTransactionItemService,
    SaleTransactionPaymentMethodService,
    PaymentExceededException)
from apps.erp.transaction.api.v1.serializers import (
    SaleTransactionSerializer,
    SaleTransactionItemSerializer,
    SaleTransactionPaymentMethodSerializer)
from apps.erp.transaction.models import (
    SaleTransaction,
    SaleTransactionItem,
    SaleTransactionPaymentMethod)


class SaleTransactionServiceAPI(APIView):

    """
    API endpoint para Transações de Venda usando o SaleTransactionService.

    Esta classe de API fornece métodos para recuperar e potencialmente interagir
    com Transações de Venda usando o SaleTransactionService. Ela se
    aproveita do framework REST do Django para lidar com requisições e respostas
    de forma estruturada.
    """

    service_class = SaleTransactionService()

    def get_object(self, pk):
        """
        Recupera um objeto pela sua chave primária (pk).

        Parâmetros:
            pk (int): A chave primária do objeto a ser recuperado.

        Retorno:
            Model: O objeto recuperado.

        Aumenta:
            Http404: Se o objeto não for encontrado.
        """
        try:
            return SaleTransaction.objects.get(id=pk)
        except ObjectDoesNotExist as exc:
            raise Http404 from exc

    def get(self, pk):
        """
        Retorna um objeto serializado.

        Parâmetros:
            pk (int): A chave primária do objeto a ser recuperado.

        Retorno:
            Response: A resposta HTTP com o objeto serializado.

        """

        sale_transaction = SaleTransactionService.get_sale_transaction_details(
            pk)
        return Response(SaleTransactionSerializer(sale_transaction).data, status.HTTP_200_OK)

    def post(self, request):
        """
        Cria um novo objeto.

        Parâmetros:
            request (django.http.HttpRequest): A requisição HTTP.

        Retorno:
            Response: A resposta HTTP com o objeto criado ou um erro de validação.

        """

        serializer = SaleTransactionSerializer(data=request.data)
        if serializer.is_valid():
            sale_transaction = SaleTransactionService.create_sale_transaction(
                serializer.validated_data)
            return Response(
                SaleTransactionSerializer(sale_transaction).data,
                status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        """
        Atualiza um objeto existente.

        Parâmetros:
            request (django.http.HttpRequest): A requisição HTTP.
            pk (int): A chave primária do objeto a ser atualizado.

        Retorno:
            Response: A resposta HTTP com o objeto atualizado ou um erro de validação.

        """

        instance = self.get_object(pk)
        serializer = SaleTransactionSerializer(instance, data=request.data)
        if serializer.is_valid():
            sale_transaction = SaleTransactionService.update_sale_transaction(
                instance, serializer.validated_data)
            return Response(
                SaleTransactionSerializer(sale_transaction).data,
                status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, pk):
        """
        Exclui um objeto.

        Parâmetros:
            pk (int): A chave primária do objeto a ser excluído.

        Retorno:
            Response: A resposta HTTP com o código 20
        """

        sale_transaction = self.get_object(pk)
        sale_transaction.delete()
        sale_transaction.save()
        return Response(status.HTTP_204_NO_CONTENT)


class SaleTransactionItemServiceAPI(APIView):

    """
    API endpoint para Itens de Transações de Venda usando o SaleTransactionItemService.

    Esta classe de API fornece métodos para recuperar e potencialmente interagir
    com Itens de Transações de Venda usando o SaleTransactionItemService. Ela se
    aproveita do framework REST do Django para lidar com requisições e respostas
    de forma estruturada.
    """

    service = SaleTransactionItemService

    def get_object(self, pk):
        """
        Recupera um objeto pela sua chave primária (pk).

        Parâmetros:
            pk (int): A chave primária do objeto a ser recuperado.

        Retorno:
            Model: O objeto recuperado.

        Aumenta:
            Http404: Se o objeto não for encontrado.
        """

        try:
            return SaleTransactionItem.objects.get(id=pk)
        except ObjectDoesNotExist as exc:
            raise Http404 from exc

    def get(self, pk):
        """
        Retorna um objeto serializado.

        Parâmetros:
            pk (int): A chave primária do objeto a ser recuperado.

        Retorno:
            Response: A resposta HTTP com o objeto serializado.

        """

        sale_transaction_item = self.service.get_sale_transiction_item(
            pk)
        serializer = SaleTransactionItemSerializer(sale_transaction_item)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request):
        """
        Cria um novo objeto.

        Parâmetros:
            request (django.http.HttpRequest): A requisição HTTP.

        Retorno:
            Response: A resposta HTTP com o objeto criado ou um erro de validação.

        """

        serializer = SaleTransactionItemSerializer(data=request.data)
        if serializer.is_valid():
            sale_transaction_item = self.service.create_sale_transaction_item(
                serializer.validated_data)
            if sale_transaction_item:
                return Response(
                    SaleTransactionItemSerializer(sale_transaction_item).data,
                    status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        """
        Atualiza um objeto existente.

        Parâmetros:
            request (django.http.HttpRequest): A requisição HTTP.
            pk (int): A chave primária do objeto a ser atualizado.

        Retorno:
            Response: A resposta HTTP com o objeto atualizado ou um erro de validação.

        """

        instance = self.get_object(pk)
        serializer = SaleTransactionItemSerializer(instance, data=request.data)
        if serializer.is_valid():
            sale_transaction_item = self.service.update_sale_transaction_item(
                instance, serializer.validated_data)
            if sale_transaction_item:
                sale_transaction_item = self.service.get_sale_transiction_item(
                    pk)
                return Response(
                    SaleTransactionItemSerializer(sale_transaction_item).data,
                    status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, pk):
        """
        Exclui um objeto.

        Parâmetros:
            pk (int): A chave primária do objeto a ser excluído.

        Retorno:
            Response: A resposta HTTP com o código 20
        """

        sale_transaction_item = self.get_object(pk)
        sale_transaction_item.delete()
        return Response(status.HTTP_204_NO_CONTENT)


class SaleTransactionPaymentMethodServiceAPI(APIView):

    """
    API endpoint para Formas de Pagamento de Transações de Venda usando o 
    SaleTransactionPaymentMethodService.

    Esta classe de API fornece métodos para recuperar e potencialmente interagir
    com Formas de Pagamento de Transações de Venda usando o 
    SaleTransactionPaymentMethodService. Ela se aproveita do framework 
    REST do Django para lidar com requisições e respostas
    de forma estruturada.
    """

    service = SaleTransactionPaymentMethodService

    def get_object(self, pk):
        """
        Recupera um objeto pela sua chave primária (pk).

        Parâmetros:
            pk (int): A chave primária do objeto a ser recuperado.

        Retorno:
            Model: O objeto recuperado.

        Aumenta:
            Http404: Se o objeto não for encontrado.
        """

        try:
            return SaleTransactionPaymentMethod.objects.get(id=pk)
        except ObjectDoesNotExist as exc:
            raise Http404 from exc

    def get(self, pk):
        """
        Retorna um objeto serializado.

        Parâmetros:
            pk (int): A chave primária do objeto a ser recuperado.

        Retorno:
            Response: A resposta HTTP com o objeto serializado.

        """

        sale_transaction_payment_method = self.service.get_sale_transiction_payment_method(
            pk)
        serializer = SaleTransactionPaymentMethodSerializer(
            sale_transaction_payment_method)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request):
        """
        Cria um novo objeto.

        Parâmetros:
            request (django.http.HttpRequest): A requisição HTTP.

        Retorno:
            Response: A resposta HTTP com o objeto criado ou um erro de validação.

        """

        serializer = SaleTransactionPaymentMethodSerializer(data=request.data)
        if serializer.is_valid():
            try:
                sale_transaction_payment_method = (
                    self.service.create_sale_transaction_payment_method(
                        serializer.validated_data)
                )
                return Response(
                    SaleTransactionPaymentMethodSerializer(
                        sale_transaction_payment_method).data,
                    status.HTTP_201_CREATED)
            except PaymentExceededException as e:
                return Response({"error": str(e)}, status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        """
        Atualiza um objeto existente.

        Parâmetros:
            request (django.http.HttpRequest): A requisição HTTP.
            pk (int): A chave primária do objeto a ser atualizado.

        Retorno:
            Response: A resposta HTTP com o objeto atualizado ou um erro de validação.

        """

        instance = self.get_object(pk)
        serializer = SaleTransactionPaymentMethodSerializer(
            instance, data=request.data)
        if serializer.is_valid():
            sale_transaction_payment_method = self.service.update_sale_transaction_payment_method(
                instance, serializer.validated_data, pk)
            if sale_transaction_payment_method:
                sale_transaction_payment_method = self.service.get_sale_transiction_payment_method(
                    pk)
                return Response(
                    SaleTransactionPaymentMethodSerializer(
                        sale_transaction_payment_method).data,
                    status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, pk):
        """
        Exclui um objeto.

        Parâmetros:
            pk (int): A chave primária do objeto a ser excluído.

        Retorno:
            Response: A resposta HTTP com o código 20
        """

        sale_transaction_payment_method = self.get_object(pk)
        sale_transaction_payment_method.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
