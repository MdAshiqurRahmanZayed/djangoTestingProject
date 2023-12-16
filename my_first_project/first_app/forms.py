from typing import Any
from django import forms 
from django.core import validators
from first_app.models import *
from django import forms
def evenORodd(value):
     if value%2==1:
          raise forms.ValidationError("Please enter even number")
     
# class userForm(forms.Form):
#     user_name = forms.CharField(label="Full name",widget=forms.TimeInput(attrs={'placeholder': 'Enter your full name','style':'width:500px'}))
#     user_dob = forms.DateField(label="Date of birth",widget=forms.TextInput(attrs={'type':'date'}))
#     user_email = forms.EmailField()
     # rating = (
     #      ('','Select options'),
     #      (1,'Worst'),
     #      (2,'Bad'),
     #      (3,'Not Bad'),
     #      (4,'Good'),
     #      (5,'Excellent!!!'),
     # )
     # # field = forms.ChoiceField(choices=rating,widget=forms.RadioSelect)
     # # field = forms.MultipleChoiceField(choices=rating)
     # field = forms.MultipleChoiceField(choices=rating,widget=forms.CheckboxSelectMultiple )
     # name = forms.CharField(validators=[validators.MaxLengthValidator(10),validators.MinLengthValidator(4)])
     # field = forms.IntegerField(validators=[validators.MaxValueValidator(10),validators.MinValueValidator(4) ,evenORodd])
     # field = forms.IntegerField(validators=[evenORodd ])
     
     # user_email = forms.EmailField()
     # user_vemail = forms.EmailField()
     
     # def clean(self):
     #      all_cleaned_data = super().clean()
     #      user_email = all_cleaned_data['user_email']     
     #      user_vemail = all_cleaned_data['user_vemail']
     #      if user_email != user_vemail:
     #           raise forms.ValidationError("Emails do not match")     
     
     
     
class musicianForm(forms.ModelForm):
     class Meta:
          model = Musician
          fields = '__all__'
class albumForm(forms.ModelForm):
     release_date = forms.DateField(widget=forms.TextInput(attrs={'type':'date'}))
     class Meta:
          model = Album
          fields = '__all__'