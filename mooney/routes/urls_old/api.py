from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MinhaAPIView

# Criação do router para as views da API
router = DefaultRouter()
router.register(r'minhaentidade', MinhaAPIView)

urlpatterns = [
    path('', include(router.urls)),
    # Adicione outras rotas da API aqui
]
