from django.urls import path,include
from .views import *

urlpatterns = [
    path("register/",signup,name='sign_up'),
    path("login/",login_page,name='login'),
    path("logout/",logout_page,name='logout'),
    path("profile/",profile,name='profile'),
    path("change-passowrd/",password_change,name='change_password'),
    path("<int:pk>/passowrd/",password_change,name='change_password'),
    path('add-picture/', add_pro_pic, name='add_pro_pic'),
    path('change-picture/',change_pro_pic, name='change_pro_pic'),
]
