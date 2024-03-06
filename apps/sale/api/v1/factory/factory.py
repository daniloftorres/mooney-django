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
