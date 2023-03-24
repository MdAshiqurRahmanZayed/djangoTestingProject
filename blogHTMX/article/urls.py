from django.urls import path
from . import views

urlpatterns = [
     path('', views.listArticle, name='article-list'), 
    path('create/', views.createArticle, name='article-create'), 
     path('<int:pk>', views.detailArticle, name='article-detail'),    
         path('delete/<int:pk>', views.deleteArticle, name='article-delete'), 
]