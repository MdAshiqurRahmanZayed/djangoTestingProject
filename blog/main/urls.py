from django.urls import path,include
from .views import *

urlpatterns = [
    path("", BlogList.as_view(),name='index'),
    path('write/', CreateBlog.as_view(), name='create_blog'),
    path('details/<slug:slug>/', blog_details, name='blog_details'),
    path('liked/<pk>/', liked, name='liked_post'),
    path('unliked/<pk>/', unliked, name='unliked_post'),
    path('my-blogs/', MyBlogs.as_view(), name='my_blogs'),
    path('edit/<pk>/', UpdateBlog.as_view(), name='edit_blog'),
]
