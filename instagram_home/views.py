from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserSignupForm
from .models import Post

# @login_required
def home(request):

    # if no user is logged in then render login page
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else: 
                messages.error(request, 'error? ')
        return render(request, 'instagram_home/login_page.html')
    
    # For switch account 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
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

def logout_user(request):
    logout(request)
    return redirect('home')


