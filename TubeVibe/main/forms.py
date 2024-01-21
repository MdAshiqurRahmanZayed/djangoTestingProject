from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Enter Email", required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email address is already in use.')
        return email
   
class UserLoginForm(forms.ModelForm):
    password    =  forms.CharField(max_length=20, widget=forms.PasswordInput)
    email       =  forms.EmailField()
    
    class Meta:
        model = User
        fields = ('email', 'password')
        
        
class VideoForm(forms.ModelForm):
    
    class Meta:
        model = Video
        fields = ('title','category','youtube_video','description','published')

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',)


class FeedbackForm(forms.ModelForm):
    
    class Meta:
        model = Feedback
        fields = ('comment',)