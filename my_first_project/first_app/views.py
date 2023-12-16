from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect 
from .models import *
from .forms import *
from django.db.models import Avg,Min,Max


def index(request):
     musician_list = Musician.objects.all().order_by('first_name')
     text = "Home page"
     context = {
          'musician_list':musician_list,
          'title':text
     }
     return render(request,'first_app/index.html',context=context)


def album_list(request,artist_id):
     aritst_info = Musician.objects.get(id=artist_id)
     album_list = Album.objects.filter(artist = artist_id ).order_by('name','release_date')
     artist_rating = Album.objects.filter(artist = artist_id ).aggregate(Avg('num_stars'))
     
     
     context = {
          'title':'List of all album',
          'aritst_info':aritst_info,
          'album_list':album_list,
          'artist_rating':artist_rating,
          
     }
     return render(request,'first_app/album_list.html',context=context)

def musician_form(request):
     if request.method == 'POST':
          form = musicianForm(request.POST)
          if form.is_valid():
               form.save(commit=True)
               return index(request)
     form =  musicianForm()
     context = {
          'form':form,
          'title':'create musician .'     
     }
     return render(request,'first_app/musician_form.html',context=context)


def album_form(request):
     if request.method == 'POST':
          form = albumForm(request.POST)
          if form.is_valid():
               form.save(commit=True)
               return index(request)
     form =  albumForm()
     context = {
          'form':form,
          'title':'create album'     
     }
     
     return render(request,'first_app/album_form.html',context=context)


def edit_artist(request,artist_id):
     
     artist = Musician.objects.get(pk=artist_id)
     form =  musicianForm(instance=artist)
     if request.method == 'POST':
          form = musicianForm(request.POST,instance=artist)
          if form.is_valid():
               form.save(commit=True)
               return redirect('album_list',artist_id)
     context = {
          'form':form,
          'title':'Edit artist'     
     }
     return render(request,'first_app/edit_artist.html',context=context)
     
def edit_album(request,album_id):
     
     album_info = Album.objects.get(pk=album_id)
     form =  albumForm(instance=album_info)
     if request.method == 'POST':
          form = albumForm(request.POST,instance=album_info)
          if form.is_valid():
               form.save(commit=True)
               return redirect('album_list',album_info.artist.id)
     context = {
          'form':form,
          'title':'Edit album', 
          'album_id':album_id, 
 
     }
     return render(request,'first_app/edit_album.html',context=context)
def delete_album(request,album_id):
     album = Album.objects.get(pk=album_id).delete()
     context = {
          'title':'Delete album',
          'success_message':'Deleted successfully.',
     }
     return render(request,'first_app/delete.html',context=context)

def delete_musician(request,artist_id):
     artist = Musician.objects.get(pk=artist_id).delete()
     context = {
          'title':'Deleted artist',
          'success_message':'Deleted successfully artist.',
     }
     return render(request,'first_app/delete.html',context=context)
# def form(request):
#      form = musicianForm()
#      data = {}
#      if request.method == 'POST':
#           form = musicianForm(request.POST)
#           if form.is_valid():
#                form.save(commit=True)
#                return index(request)
#      context = {
#           'form':form,
#           'heading':'Added new musician'
#      }
               
#      return render(request,'first_app/form.html',context=context)