# mooney/routes/admin.py
from django.contrib import admin
from django.urls import path
from django.urls import path, include
urlpatterns = [
    path('', include('django_prometheus.urls')),
    path('', admin.site.urls),
]
