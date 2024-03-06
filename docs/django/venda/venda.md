# Venda

- [Settings](#docs/django/usuario/settings.md)

## Api Venda

O fluxo de venda, será configurado e criado usando os principais temas :
Api RestFull
View->rest_framework->APIView
Design Pattners->Factory

1.  Api RestFull

    - Model `apps/sale/models.py`

      ```python
            from django.conf import settings
            from django.db import models
            from django.utils import timezone
            from apps.customer.models import Customer
            from apps.core import models as models_base


            class Sale(models_base.TimeStampedModel, models_base.SoftDeletionModel):
                user = models.ForeignKey(settings.AUTH_USER_MODEL,
                                        on_delete=models.CASCADE, verbose_name="Usuário")
                customer = models.ForeignKey(
                    Customer, on_delete=models.SET_NULL, null=True, verbose_name="Cliente")
                date_time = models.DateTimeField(
                    default=timezone.now, verbose_name="Data e Hora da Venda")
                total_price = models.DecimalField(
                    max_digits=10, decimal_places=2, verbose_name="Preço Total", default=0.00)

                def __str__(self):
                    return f"Venda #{self.pk} - {self.date_time.strftime('%d/%m/%Y %H:%M')}"

                class Meta:
                    verbose_name = "Venda"
                    verbose_name_plural = "Vendas"


            class SaleItem(models_base.TimeStampedModel, models_base.SoftDeletionModel):
                sale = models.ForeignKey(Sale, related_name='items',
                                        on_delete=models.CASCADE, verbose_name="Venda")
                product = models.ForeignKey(
                    'product.Product', on_delete=models.CASCADE, verbose_name="Produto")
                quantity = models.PositiveIntegerField(
                    default=1, verbose_name="Quantidade")
                sale_price = models.DecimalField(
                    max_digits=10, decimal_places=2, verbose_name="Preço de Venda")

                def __str__(self):
                    return f"{self.product.name} x {self.quantity}"

                class Meta:
                    verbose_name = "Item de Venda"
                    verbose_name_plural = "Itens de Venda"


            class PaymentMethod(models_base.TimeStampedModel, models_base.SoftDeletionModel):
                name = models.CharField(max_length=100, verbose_name="Nome")
                allows_installment = models.BooleanField(
                    default=False, verbose_name="Permite Parcelamento")

                def __str__(self):
                    return self.name

                class Meta:
                    verbose_name = "Meio de Pagamento"
                    verbose_name_plural = "Meios de Pagamento"


            class SalePayment(models_base.TimeStampedModel, models_base.SoftDeletionModel):
                sale = models.OneToOneField(
                    Sale, on_delete=models.CASCADE, related_name='payment', verbose_name="Venda")
                method = models.ForeignKey(
                    PaymentMethod, on_delete=models.SET_NULL, null=True, verbose_name="Método de Pagamento")
                is_installment_payment = models.BooleanField(
                    default=False, verbose_name="É Pagamento Parcelado?")
                total_installments = models.IntegerField(
                    default=1, verbose_name="Total de Parcelas")
                total_paid = models.DecimalField(
                    max_digits=10, decimal_places=2, verbose_name="Total Pago", default=0.00)

                def __str__(self):
                    return f"Pagamento da Venda #{self.sale.pk}"

                class Meta:
                    verbose_name = "Pagamento da Venda"
                    verbose_name_plural = "Pagamentos das Vendas"


            class SalePaymentInstallment(models_base.TimeStampedModel, models_base.SoftDeletionModel):
                sale_payment = models.ForeignKey(
                    SalePayment, related_name='installments', on_delete=models.CASCADE, verbose_name="Pagamento da Venda")
                installment_number = models.IntegerField(verbose_name="Número da Parcela")
                due_date = models.DateField(verbose_name="Data de Vencimento")
                amount = models.DecimalField(
                    max_digits=10, decimal_places=2, verbose_name="Valor da Parcela")
                paid = models.BooleanField(default=False, verbose_name="Pago")

                def __str__(self):
                    return f"Parcela {self.installment_number} - Venda #{self.sale_payment.sale.pk}"

                class Meta:
                    verbose_name = "Parcela do Pagamento"
                    verbose_name_plural = "Parcelas dos Pagamentos"
                    ordering = ['installment_number']

      ```

    - Url `mooney/routes/urls_api.py`

      ```python
              from apps.sale.api.v1.factory.views import SaleEntryView

              # sale
              urlpatterns = [
                  path('v1/sale/', SaleEntryView.as_view(), name="sale_create"),
              ] + urlpatterns

      ```

    - View `apps/sale/api/v1/factory/views.py`

      ```python
             from rest_framework import status
             from rest_framework.views import APIView
             from rest_framework.response import Response
             from apps.sale.api.v1.factory.factory import BasicSaleFactory
             from apps.customer.models import Customer


             class SaleEntryView (APIView):
             def post(self, request, *args, **kwargs):
                 factory = BasicSaleFactory()
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

      ```

      - Factory `apps/sale/api/v1/factory/factory.py`

        ```python
            from apps.sale.models import Sale, SaleItem
            from apps.product.models import Product


            class SaleFactory:
                def create_sale(self, user, customer, items):
                    raise NotImplementedError(
                        "This method should be implemented by subclasses.")


            class BasicSaleFactory:
                def create_sale(self, user, customer, items):
                    sale = Sale(user=user, customer=customer)
                    sale.save()
                    for item in items:

                        product_id = item.get('product')
                        try:
                            product = Product.objects.get(id=product_id)
                        except Product.DoesNotExist:
                            continue

                        sale_item = SaleItem(
                            sale=sale,
                            product=product,
                            quantity=item.get('quantity'),
                            sale_price=item.get('price'))
                        sale_item.save()

                    return sale
        ```
