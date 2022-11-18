from django.urls import path

from .views import *


urlpatterns = [
     path('',home,name="home"),
     path('create/',CreateBlog,name="create"),
     path('update/<str:slug>',UpdateBlog,name="update"),
     path('delete/<str:slug>',DeleteBlog,name="delete"),
     path('<str:slug>/',BlogDetail,name="detail"),
]