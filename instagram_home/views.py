from django.shortcuts import render
from datetime import datetime
from .models import Post
from django.contrib.auth.forms import UserCreationForm

def home(request):
    context = {
        'posts': Post.objects.all().order_by('-id'),
    }
    return render(request, 'instagram_home/instagram.html', context)

def about(request):
    return render(request, 'instagram_home/about.html')

def login_page(request):
    return render(request, 'instagram_home/login_page.html')

def signup(request):
    form = UserCreationForm()
    return render(request, 'instagram_home/signup.html', {'form': form})


