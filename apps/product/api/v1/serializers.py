from rest_framework import serializers
from apps.product.models import Product, ProductCategory, ProductImage


class ProductCategorySerializer (serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['name']


class ProductImageSerializer (serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['image', 'is_main']


class ProductSerializer (serializers.ModelSerializer):
    product_category = ProductCategorySerializer(read_only=True)
    product_image = ProductImageSerializer(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
