from django.urls import path
from django.contrib.auth import views as auth_views
from user import views as user_views
from .forms import MyAuthForm
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('login/', auth_views.LoginView.as_view(template_name='instagram_home/login_page.html', authentication_form=MyAuthForm), name='login'),
    path('signup/', views.signup, name='signup'),
    path('<str:username>/', user_views.profile, name='profile'),
]