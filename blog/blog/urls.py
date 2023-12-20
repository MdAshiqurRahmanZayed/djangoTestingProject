
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from Account.views import password_change

urlpatterns = [
    path("admin/", admin.site.urls),
    path("account/", include('Account.urls')),
    path("", include('main.urls')),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
