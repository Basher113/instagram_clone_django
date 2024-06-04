from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import UserSignupForm

@login_required
def home(request):
    context = {
        'posts': Post.objects.all().order_by('-id'),
    }
    return render(request, 'instagram_home/instagram.html', context)

def about(request):
    return render(request, 'instagram_home/about.html')

def signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect('home')
    else:
        form = UserSignupForm()
    return render(request, 'instagram_home/signup.html', {'form': form})


