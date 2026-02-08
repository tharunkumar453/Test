
from django.templatetags.static import static
from django.urls import path,include
from .views import submit, UserDashboardView,TotalSubmissions
from django.conf.urls.static import static
from django.conf import settings
urlpatterns=[
    path("submit/", submit.as_view(), name="submit"),
    path("dashboard/", UserDashboardView.as_view(), name="dashboard-list"),
    path("total/",TotalSubmissions.as_view(),name="count")
 
   
]+static( settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)


