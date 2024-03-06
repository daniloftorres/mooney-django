from django.contrib import admin
from .models import ProductCategory, Product, ProductImage


@admin.register(ProductCategory)
class CategoryAdmin(admin.ModelAdmin):
    # Adiciona image_tag para mostrar a imagem
    list_display = ('name', 'parent', 'image_tag')
    search_fields = ('name',)
    list_filter = ('parent',)

    def image_tag(self, obj):
        from django.utils.html import format_html
        if obj.image:
            return format_html('<img src="{}" style="max-height: 50px;"/>', obj.image.url)
        return "-"
    image_tag.short_description = 'Imagem'


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1  # Número de campos extras para carregar


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'product_category')
    search_fields = ('name', 'product_category__name')
    list_filter = ('product_category',)
    inlines = [ProductImageInline]


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'product', 'is_main')
    list_filter = ('product', 'is_main')

    def image_tag(self, obj):
        from django.utils.html import format_html
        if obj.image:
            return format_html('<img src="{}" style="max-height: 50px;"/>', obj.image.url)
        return "-"
    image_tag.short_description = 'Imagem'
