from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


def register(request):
     form = UserRegisterForm()
     if request.method == "POST":
          form = UserRegisterForm(request.POST)
          if form.is_valid():
               form.save()
               return redirect('main:login_page')     
     context = {
          'form':form
     } 
     return render(request,'main/account/register.html',context)

def login_page(request):
     form = AuthenticationForm()
     print(request.user)
     if request.method == 'POST':
          form  = AuthenticationForm(data = request.POST)
          if form.is_valid():
               username = form.cleaned_data.get('username')
               password = form.cleaned_data.get('password')
               user = authenticate(username=username,password=password)
               if user is not None:
                    login(request,user)
                    return redirect('main:home')
               return redirect('main:login_page')
     context = {
          'form':form,
     }
     return render(request,'main/account/register.html',context=context)

          
          
@login_required
def logout_page(request):
     logout(request)
     return redirect('main:home')


def home(request):
     videos = Video.objects.all().order_by('-created_at')
     paginator = Paginator(videos, 4)  
     page = request.GET.get('page')
     try:
          videos = paginator.page(page)
     except PageNotAnInteger:
          videos = paginator.page(1)
     except EmptyPage:
          videos = paginator.page(paginator.num_pages)
     context = {
          'videos':videos
     }
     return render(request,'home.html',context)

def video_detail(request, slug):
    video = get_object_or_404(Video, slug=slug)
    related_videos = Video.objects.filter(category=video.category).exclude(slug=slug)[:5]     
    form = FeedbackForm()

    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.feedback_video = video
            feedback.save() 
            return redirect('main:video_detail', slug=video.slug)

    context = {
        'video': video,
        'related_videos': related_videos,
        'form': form,
    }

    return render(request, 'main/video/video-detail.html', context)

@login_required
def create_video(request):
     form = VideoForm()
     if request.method == "POST":
          form = VideoForm(request.POST)
          form = form.save(commit=False)
          form.user = request.user 
          form.save() 
          return redirect('main:home')
     context = {
          'form':form
     }
     
     return render(request,'main/video/video-form.html',context)

@login_required
def update_video(request,slug):
     video = Video.objects.get(slug=slug)

     if request.user == video.user:
          form = VideoForm(instance=video)
          if request.method == "POST":
               form = VideoForm(request.POST,instance=video)
               form = form.save(commit=False)
               form.user = request.user 
               form.save() 
               return redirect('main:home')
          context = {
               'form':form
          }
     else:
          context = {
               'message':'You are not allow'
          }
     
     return render(request,'main/video/video-form.html',context)


@login_required
def delete_video(request,pk):
     video = Video.objects.get(pk=pk)
     if request.user == video.user:
          if request.method== "POST":
               video.delete()
               return redirect('main:user_all_video')
          context = {
               'video':video
          }
     else:
          
          context = {
               'message':'You are not allow'
          }
     return render(request,'main/video/video-delete.html',context)

@login_required
def user_all_video(request):
     videos = Video.objects.filter(user=request.user).order_by('-created_at')
     context = {
          'videos':videos
     }
     return render(request,'main/video/user-all-video.html',context)


def indivitual_user_all_video(request,username):
     videos = Video.objects.filter(user__username=username,published=True).order_by('-created_at')
     indivitual_user = User.objects.get(username=username)
     context = {
          'videos':videos,
          'indivitual_user':indivitual_user,
     }
     return render(request,'main/video/user-all-video.html',context)
     
     
def search(request):
    keyword = request.GET.get('keyword', '')
    print(keyword)

    if keyword:
        videos = Video.objects.order_by('-created_at').filter(
            Q(title__icontains=keyword) | Q(category__title__icontains=keyword)
        )
        videos_count = videos.count()
    else:
        videos = Video.objects.none()
        videos_count = 0

    context = {
        "videos": videos,
        "videos_count": videos_count,
        "keyword": keyword,
    }

    return render(request, "home.html", context)



@login_required
def update_profile(request):
     user = User.objects.get(username=request.user.username)
     form = UserProfileForm(instance=user)
     
     if request.method=="POST":
          form = UserProfileForm(request.POST,instance=user)
          if form.is_valid():
               form.save() 
               return redirect('main:update_profile')
          
     context = {
          'form':form
     }

     
     return render(request,'main/account/profile-change.html',context)

