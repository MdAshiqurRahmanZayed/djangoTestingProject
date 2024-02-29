from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Account

class SignUpForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ['email', 'password1', 'password2','user_type']
    def __init__(self, *args, **kwargs):
          super(SignUpForm, self).__init__(*args, **kwargs)
          self.fields['email'].widget.attrs['placeholder'] = 'Enter Email Address'
          for field in self.fields:
               self.fields[field].widget.attrs['class'] = 'form-control'
               
class LoginForm(AuthenticationForm):
    class Meta:
        model = Account
        fields = ['email', 'password']
        
    def __init__(self, *args, **kwargs):
          super(LoginForm, self).__init__(*args, **kwargs)
          for field in self.fields:
               self.fields[field].widget.attrs['class'] = 'form-control'
