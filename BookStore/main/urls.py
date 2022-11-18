from django.urls import path
from .views import *
urlpatterns = [
     path('',home,name="home"),
     path('create/',CreateBook,name="create"),
     path('<str:slug>/',BookDetail,name="detail"),
     path('update/<str:slug>/',UpdateBook,name="update"),
     path('delete/<str:slug>/',DeleteBook,name="delete"),
]
