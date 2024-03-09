from django.db import models
from django.db.models.signals import post_save
from django.utils.translation import gettext_lazy as _
from apps.core import models as models_base
from django.dispatch import receiver


class ProductCategory(models_base.TimeStampedModel, models_base.SoftDeletionModel):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True,
                               blank=True, related_name='children', verbose_name=_("Parent Category"))
    image = models.ImageField(upload_to='categories/',
                              null=True, blank=True, verbose_name=_("Image"))

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        db_table = 'product_category'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    description = models.TextField(blank=True, verbose_name=_("Description"))
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name=_("Price"))
    product_category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL,
                                         null=True, related_name='products', verbose_name=_("Category"))

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        db_table = 'product'

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='images', verbose_name=_("Product"))
    image = models.ImageField(upload_to='products/', verbose_name=_("Image"))
    is_main = models.BooleanField(
        default=False, verbose_name=_("Main Image"))

    class Meta:
        verbose_name = _("Product Image")
        verbose_name_plural = _("Product Images")
        db_table = 'product_image'

    def __str__(self):
        return f"{self.product.name} Image"

    def save(self, *args, **kwargs):
        if self.is_main:
            # Ensure only one image is marked as main
            ProductImage.objects.filter(
                product=self.product, is_main=True).update(is_main=False)
        super().save(*args, **kwargs)


class ProductStock(models.Model):
    product = models.OneToOneField(
        Product, on_delete=models.CASCADE, related_name='stock')
    quantity = models.PositiveIntegerField(default=0)
    quantity_reserved = models.PositiveIntegerField(default=0)

    @property
    def quantity_available(self):
        """Calculates available quantity by subtracting the reserved quantity from the total quantity."""
        return self.quantity - self.quantity_reserved

    def reserve_stock(self, quantity):
        """Reserves a quantity of stock if available."""
        if quantity <= self.quantity_available:
            self.quantity_reserved += quantity
            self.save()
            return True
        return False

    def release_stock(self, quantity):
        """Releases a previously reserved quantity of stock."""
        if quantity <= self.quantity_reserved:
            self.quantity_reserved -= quantity
            self.save()
            return True
        return False

    def finalize_purchase(self, quantity):
        """Finalizes the purchase of a stock quantity, adjusting the total and reserved quantities."""
        if quantity <= self.quantity_reserved:
            self.quantity -= quantity
            self.quantity_reserved -= quantity
            self.save()
            return True
        return False

    def __str__(self):
        return f"{self.product.name} - In stock: {self.quantity}, Reserved: {self.quantity_reserved}"


@receiver(post_save, sender=Product)
def create_or_update_product_stock(sender, instance, created, **kwargs):
    if created:
        ProductStock.objects.create(product=instance)
    instance.stock.save()
