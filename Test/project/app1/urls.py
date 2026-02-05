
from django.templatetags.static import static
from django.urls import path,include
from .views import submit
from django.conf.urls.static import static
from django.conf import settings
urlpatterns=[
    path("submit/",submit.as_view(),name="submit"),


]+static( settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)


