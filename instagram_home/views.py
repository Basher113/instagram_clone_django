from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .serializers import PostSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .forms import UserSignupForm, PostCreateForm
from .models import Post

# @login_required
def home(request):
    # if no user is logged in then render login page
    post_create_form = PostCreateForm()
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


class PostList(generics.ListAPIView):
    queryset = Post.objects.all().order_by('-id')
    serializer_class = PostSerializer

   

class CreatePost(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print('Hello? World!')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(f"{serializer.errors} Hello?123")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer



