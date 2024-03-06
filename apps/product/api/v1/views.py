from rest_framework.generics import ListCreateAPIView
from apps.product.models import Product, ProductImage, ProductCategory
from apps.product.api.v1.serializers import ProductSerializer, ProductCategorySerializer


class ProductListCreateAPIView (ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCategoryListCreateAPIView (ListCreateAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
