from django.urls import path, include
from user import views as user_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/<str:username>/', user_views.profile, name='profile'),
    path('about/', views.about, name='about'),
    path('logout/', views.logout_user, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('api/post-list/', views.PostList.as_view()),
    path('api/create-post/', views.CreatePost.as_view(), name='create-post'),
    path('api/post-detail/<int:pk>/', views.PostDetail.as_view(), name='api-post-detail'),
    path('api/create-comment/', views.CreateComment.as_view(), name='create-comment'),
]