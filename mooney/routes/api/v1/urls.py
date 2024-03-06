from django.urls import path, include, re_path

urlpatterns = [
    re_path(r'account\/?', include('mooney.routes.api.v1.account'))
]
