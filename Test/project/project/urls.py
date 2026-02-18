from django.contrib import admin
from django.urls import path, include
from app1 import urls as app1_urls
from Register import urls as register_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("app1/", include(app1_urls)),
    path("Register/", include(register_urls)),
    path("accounts/", include("django.contrib.auth.urls")),
]
