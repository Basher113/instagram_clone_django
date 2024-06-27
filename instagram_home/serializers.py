from rest_framework import serializers
from .models import Post, Comment, Like
from django.contrib.auth.models import User
from user.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['image', 'bio']

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True, many=False)
    class Meta:
        model = User
        fields = ['id', 'username', 'profile']


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True, many=False)

    class Meta:
        model = Comment
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'user']


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(read_only=True, many=True)
    author = UserSerializer(read_only=True, many=False)
    
    class Meta:
        model = Post
        fields = ['id', 'content', 'caption', 'created_at', 'author', 'comments']