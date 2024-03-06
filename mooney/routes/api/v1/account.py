from django.urls import path
from app.v1.account.views import (
    CheckCPFLogin,
    CheckCodeLogin
)
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
app_name = 'account'
urlpatterns = [
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
