
from django.urls import path
from .views import *

app_name = 'main'


urlpatterns = [
    path('',home,name='home'),
     path('articles/', article_list, name='article_list'),
    path('article/<int:pk>/', article_detail, name='article_detail'),
    path('article/create/', article_create, name='article_create'),
    path('article/<int:pk>/update/', article_update, name='article_update'),
    path('article/<int:pk>/delete/', article_delete, name='article_delete'),
    
    path('question/', question_list, name='question_list'),
    path('question/create/', question_create, name='question_create'),
    path('question/<int:pk>/', question_detail, name='question_detail'),
    path('question/<int:pk>/update/', question_update, name='question_update'),
    path('question/<int:pk>/delete/', question_delete, name='question_delete'),


    path('quiz/', quiz_list, name='quiz_list'),
    path('quiz/<int:quiz_id>/take/', take_quiz, name='take_quiz'),
    
    
    path('my-quiz/', my_quiz, name='my_quiz'),
    path('quiz-create/', quiz_create, name='quiz_create'),
    path('quiz/<int:quiz_id>/question/create/', quiz_question_create, name='quiz_question_create'),
]
