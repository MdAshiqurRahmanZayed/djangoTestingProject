from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
def index(request):
     musician_list = Musician.objects.all().order_by('first_name')
     text = "this is demo "
     context = {
          'musician_list':musician_list,
          'text':text
     }
     return render(request,'first_app/index.html',context=context)

def form(request):
     form = musicianForm()
     data = {}
     if request.method == 'POST':
          form = musicianForm(request.POST)
          if form.is_valid():
               form.save(commit=True)
               return index(request)
     context = {
          'form':form,
          'heading':'Added new musician'
     }
               
     return render(request,'first_app/form.html',context=context)