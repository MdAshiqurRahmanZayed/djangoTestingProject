from multiprocessing import context
from pyexpat import features
import re
from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Feature
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate

# Create your views here.
def index(request):
     features =  Feature.objects.all()     
     return render(request,'index.html',{'features':features})



def portfolio_details(request):
     return render(request,'portfolio-details.html')



def register(request):
     if request.method == 'POST':
          username = request.POST['username']
          email = request.POST['email']
          password = request.POST['password']
          password2 = request.POST['password2']
          
          if password==password2:
               if User.objects.filter(email=email).exists():
                    messages.info(request,"email already used")
                    return redirect('register')
               elif User.objects.filter(username=username).exists():
                    messages.info(request,"username already used")
                    return redirect('register')
               else:
                    user = User.objects.create_user(username=username,email=email,password=password)
                    user.save()
                    return redirect('login')
               
          else:
               messages.info("Password not same")
               return redirect(register)
     else:   
          return render(request,'register.html')

def login(request):
     if request.method =='POST':
          username = request.POST['username']
          password = request.POST['password']
          
          user = auth.authenticate(username = username,password= password)
          if user is not  None:
               auth.login(request,user)
               return redirect('/')
          else:
               messages.info(request,'Credentials invalid')
               return redirect('login')
     else:
          return render(request,"login.html")

#logout
def logout(request):
     auth.logout(request)
     return redirect('/')


def counter(request):
     posts =[1,2,3,"tim","zayed"]
     return render(request,'counter.html',{'posts':posts})

def post(request,pk):
     return render(request,'post.html',{'pk':pk})
     