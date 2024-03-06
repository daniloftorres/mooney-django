from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.core import models as models_base


class ProductCategory(models_base.TimeStampedModel, models_base.SoftDeletionModel):
    name = models.CharField(max_length=255, verbose_name="Nome")
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True,
                               blank=True, related_name='children', verbose_name="Categoria Pai")
    image = models.ImageField(upload_to='categories/',
                              null=True, blank=True, verbose_name="Imagem")

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        db_table = 'product_category'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nome")
    description = models.TextField(blank=True, verbose_name="Descrição")
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Preço")
    product_category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL,
                                         null=True, related_name='products', verbose_name="Categoria")

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        db_table = 'product'

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='images', verbose_name="Produto")
    image = models.ImageField(upload_to='products/', verbose_name="Imagem")
    is_main = models.BooleanField(
        default=False, verbose_name="Imagem Principal")

    class Meta:
        verbose_name = "Imagem do Produto"
        verbose_name_plural = "Imagens do Produto"
        db_table = 'product_image'

    def __str__(self):
        return f"{self.product.name} Image"

    def save(self, *args, **kwargs):
        if self.is_main:
            # Garantir que apenas uma imagem seja marcada como principal
            ProductImage.objects.filter(
                product=self.product, is_main=True).update(is_main=False)
        super().save(*args, **kwargs)
