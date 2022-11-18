# from multiprocessing import context
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import BookStore
from .forms import *
# Create your views here.
def home(request):
     allbook = BookStore.objects.all().order_by('-date_created')
     context = {
          'allbook' : allbook
     }
     return render(request,'index.html',context)

def BookDetail(request,slug):
     book = BookStore.objects.get(slug=slug)
     
     context = {
          'book' : book
     }
     return render(request,'detail.html',context)

def CreateBook(request):
     form  = BookStoreForm(request.POST or None)
     
     if form.is_valid():
          form.save()
          return redirect('home')
     
     context = {
          'form':form
     }
     return render(request,'form.html',context)

def UpdateBook(request,slug):
     book = BookStore.objects.get(slug=slug)
     form  = BookStoreForm(request.POST or None,instance = book)
     
     if form.is_valid():
          form.save()
          return redirect('home')
     
     context = {
          'form':form
     }
     return render(request,'form.html',context)

def DeleteBook(request,slug):
     book = BookStore.objects.get(slug = slug)
     if request.method =="POST":
          book.delete()
          return redirect("home")
     context = {
          'book':book
     }

     return render(request,'confirm.html',context)