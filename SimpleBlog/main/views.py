from multiprocessing import context
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Blog
from .forms import *
# Create your views here.
def home(request):
     AllPost = Blog.objects.all().order_by('-date_created') 
     context = {
          'AllPost':AllPost
     }
     return render(request,'index.html',context)

def BlogDetail(request,slug):
     post = Blog.objects.get(slug=slug)
     
     context = {
          'post' : post
     }
     return render(request,'detail.html',context)

def CreateBlog(request):
     form  = BlogtoreForm(request.POST, request.FILES)
     
     if form.is_valid():
          form.save()
          return redirect('home')
     
     context = {
          'form':form
     }
     return render(request,'form.html',context)

def UpdateBlog(request,slug):
     blog = get_object_or_404(Blog, slug = slug)
     form  = BlogtoreForm(request.POST or None,  instance = blog)
     if request.method =="POST":
          form1 = BlogtoreForm(request.POST or None, request.FILES,  instance = blog)
          if form1.is_valid():
               form1.save()
               return redirect('detail',slug)
     
     context = {
          'form':form
     }
     return render(request,'form.html',context)


def DeleteBlog(request,slug):
     book = Blog.objects.get(slug = slug)
     if request.method =="POST":
          book.delete()
          return redirect("home")
     context = {
          'book':book
     }

     return render(request,'confirm.html',context)
