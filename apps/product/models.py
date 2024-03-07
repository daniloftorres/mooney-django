from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.core import models as models_base


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
