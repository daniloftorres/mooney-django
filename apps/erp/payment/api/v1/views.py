from django.db import transaction
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from apps.erp.payment.models import PaymentMethod
from apps.erp.payment.api.v1.serializers import PaymentMethodSerializer


class PaymentMethodListCreateAPIView (ListCreateAPIView):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer

    def create(self, request, *args, **kwargs):
        is_many = isinstance(request.data, list)

        with transaction.atomic():
            serializer = self.get_serializer(data=request.data, many=is_many)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
