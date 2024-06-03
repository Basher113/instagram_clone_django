from django.shortcuts import render
from datetime import datetime
from .models import Post

def home(request):
    context = {
        'posts': Post.objects.all().order_by('-id'),
    }
    

    return render(request, 'instagram_home/instagram.html', context)


def about(request):
    return render(request, 'instagram_home/about.html')
