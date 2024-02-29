from .models import *
from django.forms.models import ModelForm


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ('category','title','content',)
        
    def __init__(self, *args, **kwargs):
          super(ArticleForm, self).__init__(*args, **kwargs)
          for field in self.fields:
               self.fields[field].widget.attrs['class'] = 'form-control'
               



class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['title','content']

    def __init__(self, *args, **kwargs):
          super(QuestionForm, self).__init__(*args, **kwargs)
          for field in self.fields:
               self.fields[field].widget.attrs['class'] = 'form-control'
               
               
class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['content', ]
        
        
class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        
class QuizForm(ModelForm):
    class Meta:
        model = Quiz
        fields = ['title']
        
        
class QuizQuestionForm(ModelForm):
    class Meta:
        model = QuizQuestion
        fields = ['quiz_content', 'option1', 'option2', 'option3', 'option4', 'correct_answer']

        
        

