from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'username': 'basherkalim',
        'content': 'Some picture',
        'caption': 'this is caption'
    },
    {
        'username': 'mariamkalim',
        'content': 'Some picture2',
        'caption': 'this is caption2'
    }
]


def home(request):

    return render(request, 'instagram_home/instagram.html', context={'posts': posts})


def about(request):
    return render(request, 'instagram_home/about.html')
