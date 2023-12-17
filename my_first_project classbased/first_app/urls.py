from django.urls import path
from first_app.views import *
urlpatterns = [
    path('',Index.as_view(),name='index'),
    path('musician-detail/<int:pk>/',MusicianDetail.as_view(),name='musician_detail'),
    path('add-musician/',MusicianCreateView.as_view(),name='musician_create'),
    path('update-musician/<int:pk>/',MusicianUpdateView.as_view(),name='musician_update'),
    path('delete-musician/<int:pk>/',MusicianDeleteView.as_view(),name='musician_delete'),

]
