from django.db import transaction
from django.db.models import Sum, F
from django.http import Http404
from apps.erp.transaction.models import SaleTransaction, SaleTransactionItem, SaleTransactionPaymentMethod, SaleTransactionPaymentInstallment
# from apps.erp.transaction.api.v1.serializers import SaleTransactionSerializer
from django.db.models import Q


class PaymentExceededException(Exception):
    """Exceção lançada quando o valor total dos pagamentos ultrapassa o valor devido."""
    pass


class SaleTransactionService:
    @staticmethod
    def get_sale_transaction_details(sale_transaction_id):

        try:
            return SaleTransaction.objects.get(id=sale_transaction_id)
        except SaleTransaction.DoesNotExist:
            raise Http404

    def create_sale_transaction(validated_data):
        # remove relationship
        items_data = validated_data.pop('items', [])
        payment_method_data = validated_data.pop('payment_methods', [])
        payment_installments = validated_data.pop('payment_installments', [])

        # create sala transaction
        sale_transaction = SaleTransaction.objects.create(**validated_data)

        # create items
        """if len(items_data) > 0:
            for item in items_data:
                SaleTransactionItem.objects.create(
                    sale_transaction=sale_transaction, **item)"""

        return sale_transaction

    def update_sale_transaction(instance, validated_data):

        # Atualiza campos diretos (não-relacionais)
        for field, value in validated_data.items():
            if field not in ['items', 'payment_methods', 'payment_installments']:
                setattr(instance, field, value)
        instance.save()

        # Atualiza itens da transação
        """if 'items' in validated_data:
            items_data = validated_data.pop('items')
            # Aqui você pode implementar a lógica para atualizar, criar ou excluir itens
            # Isso dependerá da sua lógica de negócios específica
            # Exemplo simples:
            instance.items.all().delete()  # Remover itens existentes e substituí-los
            for item_data in items_data:
                SaleTransactionItem.objects.create(
                    sale_transaction=instance, **item_data)"""

        return instance

    @staticmethod
    def update_sale_transaction_totals(sale_transaction_id):
        sale_transaction = SaleTransaction.objects.get(id=sale_transaction_id)
        items = SaleTransactionItem.objects.filter(
            sale_transaction_id=sale_transaction_id)

        total_quantity = items.aggregate(
            total=Sum(F('quantity')))['total'] or 0
        total_amount = items.aggregate(total=Sum(
            F('quantity') * F('sale_price') * (1 - F('discount') / 100)))['total'] or 0
        total_discount_amount = items.aggregate(
            total=Sum(F('quantity') * F('sale_price') * F('discount') / 100))['total'] or 0

        # get total amount
        payments = SaleTransactionPaymentMethod.objects.filter(
            sale_transaction_id=sale_transaction_id)
        payments = payments.aggregate(
            total=Sum(F('total_amount')))['total']
        payments = 0 if payments is None else payments

        total_due = total_amount - payments

        sale_transaction.total_quantity = total_quantity
        sale_transaction.total_amount = total_amount
        sale_transaction.total_discount_amount = total_discount_amount
        sale_transaction.net_amount = total_amount - total_discount_amount
        sale_transaction.total_due = total_due
        sale_transaction.save()

    @staticmethod
    def handle_change_in_sale_transaction_item(instance):
        SaleTransactionService.update_sale_transaction_totals(
            instance.sale_transaction.id)

    @staticmethod
    def handle_before_save_sale_transaction_item(instance):
        if instance.pk:
            original_item = SaleTransactionItem.objects.get(pk=instance.pk)
            if instance.quantity != original_item.quantity or instance.sale_price != original_item.sale_price or instance.discount != original_item.discount:
                instance.total_amount = instance.quantity * \
                    instance.sale_price * (1 - instance.discount / 100)
                SaleTransactionService.update_sale_transaction_totals(
                    instance.sale_transaction.id)
        else:
            instance.total_amount = instance.quantity * \
                instance.sale_price * (1 - instance.discount / 100)


class SaleTransactionItemService:

    @staticmethod
    def get_sale_transiction_item(sale_transaction_item_id):
        try:
            return SaleTransactionItem.objects.get(id=sale_transaction_item_id)
        except SaleTransactionItem.DoesNotExist:
            raise Http404

    def create_sale_transaction_item(validated_data):
        return SaleTransactionItem.objects.create(**validated_data)

    def update_sale_transaction_item(instance, validated_data):
        return SaleTransactionItem.objects.filter(id=instance.id).update(**validated_data)

    def remove_sale_transaction_item(sale_transaction_item_id):
        pass


class SaleTransactionPaymentInstallmentService:

    @staticmethod
    def get_total_status(validated_data):
        return True
        return SaleTransaction.objects.filter(id=sale_transaction_id).update(total_due=total_due)

    # SaleTransactionPaymentInstallment
    def get_sale_transiction_payment_installment(sale_transaction_item_id):
        try:
            return SaleTransactionPaymentMethod.objects.get(id=sale_transaction_item_id)
        except SaleTransactionPaymentMethod.DoesNotExist:
            raise Http404

    def create_sale_transaction_payment_installment(validated_data):

        payment_installment = SaleTransactionPaymentMethod.objects.create(
            **validated_data)
        if payment_installment:
            SaleTransactionPaymentMethodService.get_total_status(
                validated_data)

        return payment_installment

    def update_sale_transaction_payment_installment(instance, validated_data):
        return SaleTransactionPaymentMethod.objects.filter(id=instance.id).update(**validated_data)

    def remove_sale_transaction_payment_installment(sale_transaction_payment_installment_id):
        pass


class SaleTransactionPaymentMethodService:

    @staticmethod
    def get_sale_transiction_payment_method(sale_transaction_item_id):
        try:
            return SaleTransactionPaymentMethod.objects.get(id=sale_transaction_item_id)
        except SaleTransactionPaymentMethod.DoesNotExist:
            raise Http404

    @transaction.atomic
    def create_sale_transaction_payment_method(validated_data):

        sale_transaction_id = validated_data['sale_transaction'].id
        payment_total_amount = validated_data['total_amount']
        payment_method = validated_data['payment_method']
        sale_transaction = SaleTransaction.objects.get(id=sale_transaction_id)

        # check before create
        # get total amount
        payments = SaleTransactionPaymentMethod.objects.filter(
            sale_transaction_id=sale_transaction_id)
        payments = payments.aggregate(
            total=Sum(F('total_amount')))['total']
        payments = 0 if payments is None else payments

        # check if value is maior
        if (sale_transaction.total_amount - (payments + payment_total_amount)) < 0:
            raise PaymentExceededException(
                "O valor total dos pagamentos ultrapassa o valor devido.")

        # check if method already exist
        payment_method_exist = SaleTransactionPaymentMethod.objects.filter(
            sale_transaction_id=sale_transaction_id, payment_method=validated_data['payment_method']).first()
        if payment_method_exist:
            SaleTransactionPaymentInstallment.objects.filter(
                sale_transaction_payment_method=payment_method_exist).delete()
            payment_method_exist.delete()

        # create
        payment_method_created = SaleTransactionPaymentMethod.objects.create(
            **validated_data)

        # create installments
        if validated_data['payment_method'].id == 3 and validated_data['installment'] > 1:

            remaining_value = 0
            installment_mod = payment_total_amount % validated_data['installment']
            if installment_mod > 0:
                value_per_installment = payment_total_amount / \
                    validated_data['installment']
                value_per_installment = round(value_per_installment, 2)
                remaining_value = payment_total_amount - (
                    value_per_installment*validated_data['installment'])
                remaining_value = round(remaining_value, 2)

            else:
                value_per_installment = payment_total_amount / \
                    validated_data['installment']
                value_per_installment = round(value_per_installment, 2)

            for installment in range(1, validated_data['installment']+1):

                # last installment
                if installment == validated_data['installment']:
                    sale_transaction_payment_installment = {
                        'sale_transaction': validated_data['sale_transaction'],
                        'sale_transaction_payment_method': payment_method_created,
                        'status': 'Pending',
                        'total_installments': validated_data['installment'],
                        'payment_method': payment_method,
                        'installment': installment,
                        'total_amount': value_per_installment+remaining_value,
                        'total_discount_amount': 0,
                        'net_amount': 0,
                        'tax_amount': 0,
                        'notes': '',
                    }
                    SaleTransactionPaymentInstallment.objects.create(
                        **sale_transaction_payment_installment)
                else:
                    sale_transaction_payment_installment = {
                        'sale_transaction': validated_data['sale_transaction'],
                        'sale_transaction_payment_method': payment_method_created,
                        'status': 'Pending',
                        'total_installments': validated_data['installment'],
                        'payment_method': payment_method,
                        'installment': installment,
                        'total_amount': value_per_installment,
                        'total_discount_amount': 0,
                        'net_amount': 0,
                        'tax_amount': 0,
                        'notes': '',
                    }
                    SaleTransactionPaymentInstallment.objects.create(
                        **sale_transaction_payment_installment)
                    # SaleTransactionPaymentInstallmentService.create_sale_transaction_payment_installment()
        else:
            sale_transaction_payment_installment = {
                'sale_transaction': validated_data['sale_transaction'],
                'sale_transaction_payment_method': payment_method_created,
                'status': 'Pending',
                'total_installments': validated_data['installment'],
                'payment_method': payment_method,
                'installment': 1,
                'total_amount': validated_data['total_amount'],
                'total_discount_amount': 0,
                'net_amount': 0,
                'tax_amount': 0,
                'notes': '',
            }
            SaleTransactionPaymentInstallment.objects.create(
                **sale_transaction_payment_installment)
            # SaleTransactionPaymentInstallmentService.create_sale_transaction_payment_installment()

        # preparing final return
        # get total amount
        payments = SaleTransactionPaymentMethod.objects.filter(
            sale_transaction_id=sale_transaction_id)
        payments = payments.aggregate(
            total=Sum(F('total_amount')))['total']
        payments = 0 if payments is None else payments

        total_due = sale_transaction.total_amount - payments

        # update total due
        SaleTransaction.objects.filter(
            id=sale_transaction_id).update(total_due=total_due)

        print("valores para calculo")
        print(sale_transaction.total_amount)
        print(payments)

        total_due = sale_transaction.total_amount - payments
        SaleTransaction.objects.filter(
            id=sale_transaction_id).update(total_due=total_due)

        return payment_method_created

    def update_sale_transaction_payment_method(instance, validated_data, sale_transaction_payment_method_id):

        print("### into update")

        sale_transaction_id = validated_data['sale_transaction'].id
        payment_total_amount = validated_data['total_amount']
        payment_method = validated_data['payment_method']
        sale_transaction = SaleTransaction.objects.get(id=sale_transaction_id)

        # check before create
        # get total amount
        payments = SaleTransactionPaymentMethod.objects.filter(
            sale_transaction_id=sale_transaction_id).filter(~Q(id=sale_transaction_payment_method_id))
        payments = payments.aggregate(
            total=Sum(F('total_amount')))['total']
        payments = 0 if payments is None else payments

        # check if value is maior
        if (sale_transaction.total_amount - (payments + payment_total_amount)) < 0:
            raise PaymentExceededException(
                "O valor total dos pagamentos ultrapassa o valor devido.")

        # update
        payment_method_updated = SaleTransactionPaymentMethod.objects.filter(id=sale_transaction_payment_method_id).update(
            **validated_data)

        print("#retorno update", payment_method_updated)

        # if there is installmente, than recreate they
        if payment_method_updated > 0:

            # removemos todas parcelas
            payment_installment_deleted = SaleTransactionPaymentInstallment.objects.filter(
                sale_transaction_payment_method_id=sale_transaction_payment_method_id).delete()

            print("#return payment_installment_deleted :: ",
                  payment_installment_deleted)
            print("#dentro do if de recriacao de parcelas id ",
                  sale_transaction_payment_method_id)

            # create installments
            if validated_data['payment_method'].id == 3 and validated_data['installment'] > 1:

                remaining_value = 0
                installment_mod = payment_total_amount % validated_data['installment']
                if installment_mod > 0:
                    value_per_installment = payment_total_amount / \
                        validated_data['installment']
                    value_per_installment = round(value_per_installment, 2)
                    remaining_value = payment_total_amount - (
                        value_per_installment*validated_data['installment'])
                    remaining_value = round(remaining_value, 2)

                else:
                    value_per_installment = payment_total_amount / \
                        validated_data['installment']
                    value_per_installment = round(value_per_installment, 2)

                for installment in range(1, validated_data['installment']+1):

                    # last installment
                    if installment == validated_data['installment']:
                        sale_transaction_payment_installment = {
                            'sale_transaction': validated_data['sale_transaction'],
                            'sale_transaction_payment_method_id': sale_transaction_payment_method_id,
                            'status': 'Pending',
                            'total_installments': validated_data['installment'],
                            'payment_method': payment_method,
                            'installment': installment,
                            'total_amount': value_per_installment+remaining_value,
                            'total_discount_amount': 0,
                            'net_amount': 0,
                            'tax_amount': 0,
                            'notes': '',
                        }
                        SaleTransactionPaymentInstallment.objects.create(
                            **sale_transaction_payment_installment)
                    else:
                        sale_transaction_payment_installment = {
                            'sale_transaction': validated_data['sale_transaction'],
                            'sale_transaction_payment_method_id': sale_transaction_payment_method_id,
                            'status': 'Pending',
                            'total_installments': validated_data['installment'],
                            'payment_method': payment_method,
                            'installment': installment,
                            'total_amount': value_per_installment,
                            'total_discount_amount': 0,
                            'net_amount': 0,
                            'tax_amount': 0,
                            'notes': '',
                        }
                        SaleTransactionPaymentInstallment.objects.create(
                            **sale_transaction_payment_installment)
                        # SaleTransactionPaymentInstallmentService.create_sale_transaction_payment_installment()
            else:
                sale_transaction_payment_installment = {
                    'sale_transaction': validated_data['sale_transaction'],
                    'sale_transaction_payment_method_id': sale_transaction_payment_method_id,
                    'status': 'Pending',
                    'total_installments': validated_data['installment'],
                    'payment_method': payment_method,
                    'installment': 1,
                    'total_amount': validated_data['total_amount'],
                    'total_discount_amount': 0,
                    'net_amount': 0,
                    'tax_amount': 0,
                    'notes': '',
                }
                SaleTransactionPaymentInstallment.objects.create(
                    **sale_transaction_payment_installment)
                # SaleTransactionPaymentInstallmentService.create_sale_transaction_payment_installment()

            # preparing final return
            # get total amount
            payments = SaleTransactionPaymentMethod.objects.filter(
                sale_transaction_id=sale_transaction_id)
            payments = payments.aggregate(
                total=Sum(F('total_amount')))['total']
            payments = 0 if payments is None else payments

            total_due = sale_transaction.total_amount - payments

            # update total due
            SaleTransaction.objects.filter(
                id=sale_transaction_id).update(total_due=total_due)

            print("valores para calculo")
            print(sale_transaction.total_amount)
            print(payments)

            total_due = sale_transaction.total_amount - payments
            SaleTransaction.objects.filter(
                id=sale_transaction_id).update(total_due=total_due)

        payment_method_updated = SaleTransactionPaymentMethod.objects.get(
            id=sale_transaction_payment_method_id)
        return payment_method_updated

    def remove_sale_transaction_payment_method(sale_transaction_payment_method_id):
        pass
