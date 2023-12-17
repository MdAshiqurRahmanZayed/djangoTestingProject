from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect 
from .models import *
from .forms import *
from django.db.models import Avg,Min,Max
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
# class Index(TemplateView):
#      template_name = 'first_app/index.html'
#      def get_context_data(self, **kwargs) -> dict[str, Any]:
#          context = super().get_context_data(**kwargs)
#          context["sample_text1"] ='sample text1' 
#          context["sample_text2"] ='sample text2' 
#          return context
     
     
class Index(ListView):
     model = Musician
     context_object_name = 'musician_list'
     template_name = 'first_app/index.html'
      
     
class MusicianDetail(DetailView):
    context_object_name = 'musician_detail'
    model = Musician
    template_name = 'first_app/musician_detail.html'

class MusicianCreateView(CreateView):
    model = Musician
    fields = ('first_name','last_name','instrument')
    template_name = 'first_app/musician_form.html'
    
    
class MusicianUpdateView(UpdateView):
    model = Musician
    fields = ('first_name','last_name')
    template_name = 'first_app/musician_form.html'

class MusicianDeleteView(DeleteView):
    model = Musician
    success_url = reverse_lazy('index')
    template_name = 'first_app/musician_delete.html'