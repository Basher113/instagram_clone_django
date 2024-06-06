from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from instagram_home.models import Post
from django.contrib.auth.models import User

def profile(request, username):
    viewing_user = get_object_or_404(User, username=username)
    current_user = request.user
    posts = Post.objects.filter(author=viewing_user)
    context = {
        'posts': posts,
        'current_user': current_user,
        'viewing_user': viewing_user,
        
    }
    return render(request, 'user/profile.html', context)
