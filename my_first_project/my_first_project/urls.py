
from django.contrib import admin
from django.urls import path,include
from first_app.views import index
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('first_app.urls')),
]
