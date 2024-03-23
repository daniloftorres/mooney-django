from django.conf import settings
from django.urls import path, include
from rest_framework import routers

from django.conf.urls.static import static

# Importa a view do django-prometheus
from django_prometheus import exports as django_prometheus_exports


urlpatterns = [
    # Suas URLs existentes
    # ...
    # URL para expor métricas do Prometheus
    path('', include('django_prometheus.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + urlpatterns
