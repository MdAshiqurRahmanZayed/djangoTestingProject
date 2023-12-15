from django.urls import path
from first_app.views import *
urlpatterns = [
    path("index/", index,name='index'),
    path("form/", form,name='form'),
]
