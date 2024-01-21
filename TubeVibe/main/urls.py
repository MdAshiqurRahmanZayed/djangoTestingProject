from django.urls import path
from .views import *

app_name = 'main'


urlpatterns = [
    path('register/',register,name='register'),
    path('login/',login_page,name='login_page'),
    path('logout/',logout_page,name='logout_page'),
    path('profile-update/',update_profile,name='update_profile'),
    
    path('',home,name='home'),
    path('search/', search, name='search'),
    path('create-video/',create_video,name='create_video'),
    path('video/<slug:slug>/',video_detail,name='video_detail'),
    path('update-video/<slug:slug>/',update_video,name='update_video'),
    path('delete-video/<pk>/',delete_video,name='delete_video'),
    path('user-all-video/',user_all_video,name='user_all_video'),
    path('user-all-video/<str:username>/',indivitual_user_all_video,name='indivitual_user_all_video'),
    
]
