from django.db import models
from Accounts.models import *
from tinymce.models import HTMLField



class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
   
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
   
class Question(models.Model):
    title = models.CharField( max_length=50)
    content = HTMLField()
    
    def __str__(self):
        return self.title

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.content
    
    
class Quiz(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class QuizQuestion(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    quiz_content = models.CharField(max_length=200)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correct_answer = models.CharField(max_length=100)

    def __str__(self):
        return self.quiz_content

class QuizAnswer(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    question = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE)
    selected_option = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username}'s answer for {self.question.quiz_content}"

