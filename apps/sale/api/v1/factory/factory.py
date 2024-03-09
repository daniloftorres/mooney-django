from apps.erp.transaction.models import SaleTransaction, SaleTransactionItem
from apps.product.models import Product


class SaleTransactionFactory:
    def create_sale(self, user, customer, items):
        raise NotImplementedError(
            "This method should be implemented by subclasses.")


class BasicSaleFactory:
    def create_sale(self, user, customer, items):
        sale = SaleTransaction(user=user, customer=customer)
        sale.save()
        for item in items:

            product_id = item.get('product')
            try:
                product = Product.objects.get(id=product_id)
            except Product.DoesNotExist:
                continue

            sale_item = SaleTransactionItem(
                sale=sale,
                product=product,
                quantity=item.get('quantity'),
                sale_price=item.get('price'))
            sale_item.save()

        return sale
