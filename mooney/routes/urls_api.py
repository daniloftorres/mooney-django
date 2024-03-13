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
from apps.erp.payment.api.v1.views import PaymentMethodListCreateAPIView
from apps.erp.transaction.api.v1.services.views import SaleTransactionServiceAPI, SaleTransactionItemServiceAPI
from apps.erp.transaction.api.v1.views import SaleTransactionAPI, SaleTransactionItemAPI

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
    path('v1/product/<int:pk>/', ProductListCreateAPIView.as_view(),
         name="product_list"),
    path('v1/product/category/', ProductCategoryListCreateAPIView.as_view(),
         name="product_category_create"),
    path('v1/product/category/<int:pk>/', ProductCategoryListCreateAPIView.as_view(),
         name="product_category_list"),
] + urlpatterns

# payment
urlpatterns = [
    path('v1/payment/method/', PaymentMethodListCreateAPIView.as_view(),
         name="payment-method-create"),
    path('v1/payment/method/<int:pk>/',
         PaymentMethodListCreateAPIView.as_view(), name="payment-method-create")
] + urlpatterns

# sale with factory
urlpatterns = [
    path('v1/factory/sale/', SaleEntryView.as_view(), name="sale_create"),
    path('v1/factory/sale/<int:pk>/', SaleEntryView.as_view(), name="sale_get")
] + urlpatterns

# default
urlpatterns = [
    path('v1/sale/', SaleTransactionAPI.as_view(),
         name="sale_transaction_create"),
    path('v1/sale/<int:pk>/', SaleTransactionAPI.as_view(),
         name="sale_transaction_get"),

    path('v1/sale/item/', SaleTransactionItemAPI.as_view(),
         name="sale_transaction_item_create"),
    path('v1/sale/item/<int:pk>/', SaleTransactionItemAPI.as_view(),
         name="sale_transaction_item_get")
] + urlpatterns

# default + service
urlpatterns = [
    path('v1/service/sale/', SaleTransactionServiceAPI.as_view(),
         name="sale_transaction_service_create"),
    path('v1/service/sale/<int:pk>/', SaleTransactionServiceAPI.as_view(),
         name="sale_transaction_service_get"),

    path('v1/service/sale/item/', SaleTransactionItemServiceAPI.as_view(),
         name="sale_transaction_service_item_create"),
    path('v1/service/sale/item/<int:pk>/', SaleTransactionItemServiceAPI.as_view(),
         name="sale_transaction_service_item_get")
] + urlpatterns

urlpatterns = [
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + urlpatterns
