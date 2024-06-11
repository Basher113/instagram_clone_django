from rest_framework import serializers
from .models import Post, Comment, Like
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):

    comments = CommentSerializer(read_only=True, many=True, source="comment_set")

    class Meta:
        model = Post
        fields = '__all__'