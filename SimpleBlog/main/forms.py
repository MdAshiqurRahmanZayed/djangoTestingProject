from django.forms import *
from .models import *

class BlogtoreForm(ModelForm):
     """Form definition for BookStore."""

     class Meta:
          """Meta definition for BookStoreform."""

          model = Blog
          fields = ('title','author','descriptions','image')
          
          widgets = {
            'title' : TextInput(attrs={'class':'form-control ' ,'placeholder':'Title'}),
            'author' : TextInput(attrs={'class':'form-control ' ,'placeholder':'Author'}),
            'descriptions' : Textarea(attrs={'class':'form-control form-control form-control-lg ','placeholder':'Descriptions'}),
          }
