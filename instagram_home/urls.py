from django.urls import path, include
from user import views as user_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/<str:username>/', user_views.profile, name='profile'),
    path('about/', views.about, name='about'),
    path('logout/', views.logout_user, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('api_list/', views.PostList.as_view())
]