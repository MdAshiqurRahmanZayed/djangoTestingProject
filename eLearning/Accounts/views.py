from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import login, logout

def register_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main:home')  
    else:
        form = SignUpForm()
    return render(request, 'Accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main:home')  
    else:
        form = LoginForm()
    return render(request, 'Accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('main:home')  
