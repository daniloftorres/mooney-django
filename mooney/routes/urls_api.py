from django.conf import settings
from django.urls import path, include
from rest_framework import routers
from apps.customer.api.v1.views import CustomerViewSet
from apps.sale.api.v1.factory.views import SaleEntryView
from apps.customer.api.v1.views_oauth2_client_credentials import OAuth2ClientCredentials
from apps.customer.api.v1.views_oauth2_password import OAuth2Password
from apps.product.api.v1.views import ProductCategoryListCreateAPIView, ProductListCreateAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.conf.urls.static import static

router = routers.DefaultRouter()
# router.register(r'customer-oauth2', CustomerViewSetOAuth2)
router.register(r'customer', CustomerViewSet)


urlpatterns = [
    path('v1/', include(router.urls)),
]

# autenticação jwt
urlpatterns = [
    path('v1/token/', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('v1/token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
] + urlpatterns

# autenticação oauth2
urlpatterns = [
    path('v1/oauth2/', include('oauth2_provider.urls',
         namespace='oauth2_provider')),
    path('v1/oauth2-client-credentials/', OAuth2ClientCredentials.as_view(),
         name='oauth2-client-credentials'),
    path('v1/oauth2-password/', OAuth2Password.as_view(),
         name='oauth2-password'),
] + urlpatterns

# product
urlpatterns = [
    path('v1/product/', ProductListCreateAPIView.as_view(),
         name="product_list_create"),
    path('v1/product/category/', ProductCategoryListCreateAPIView.as_view(),
         name="product_category_list_create"),
] + urlpatterns

# sale with factory
urlpatterns = [
    path('v1/factory/sale/', SaleEntryView.as_view(), name="sale_create"),
    path('v1/factory/sale/<int:pk>/', SaleEntryView.as_view(), name="sale_get")
] + urlpatterns

urlpatterns = [
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + urlpatterns
