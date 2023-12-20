from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required
from .forms import *


def signup(request):
     form  = SignUpForm()
     register = False
     if request.method == 'POST':
          form = SignUpForm(data = request.POST)
          if form.is_valid():
               form.save()
               register = True
               
     context = {
          'form':form,
          'register':register,
     }
     
     return render(request,'Account/signup.html',context=context)


def login_page(request):
     form = AuthenticationForm()
     if request.method == 'POST':
          form  = AuthenticationForm(data = request.POST)
          if form.is_valid():
               username = form.cleaned_data.get('username')
               password = form.cleaned_data.get('password')
               print(username,password)
               user = authenticate(username=username,password=password)
               if user is not None:
                    login(request,user)
                    return redirect('index')
     context = {
          'form':form,
     }
     return render(request,'Account/login.html',context=context)


@login_required
def logout_page(request):
     logout(request)
     return redirect('index')
     
@login_required
def profile(request):
     current_user = request.user 
     form  = UserProfileForm(instance = current_user)
     if request.method == 'POST':
          form = UserProfileForm(data = request.POST,instance = current_user)
          if form.is_valid():
               form.save()
               return redirect('profile')
     context = {
          'form':form,
     }
     return render(request,'Account/profile.html',context=context)


@login_required
def password_change(request,pk=None):
     current_user = request.user
     form = PasswordChangeForm(current_user)
     if request.method == 'POST':
          form  = PasswordChangeForm(request.POST) 
          if form.is_valid():
               form.save()
               
     context = {
          'form':form,
     }
     
     return render(request,'Account/change_password.html',context=context)


@login_required
def add_pro_pic(request):
    form = ProfilePic()
    if request.method == 'POST':
        form = ProfilePic(request.POST, request.FILES)
        if form.is_valid():
            user_obj = form.save(commit=False)
            user_obj.user = request.user
            user_obj.save()
            return redirect('profile')
    return render(request, 'Account/pro_pic_add.html', context={'form':form})

@login_required
def change_pro_pic(request):
    form = ProfilePic(instance=request.user.user_profile)
    if request.method == 'POST':
        form = ProfilePic(request.POST, request.FILES, instance=request.user.user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    return render(request, 'Account/pro_pic_add.html', context={'form':form})
