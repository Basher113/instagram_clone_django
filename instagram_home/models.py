from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from PIL import Image

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.ImageField(upload_to='posts-content')
    caption = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f"POST: {self.id},  Author: {self.author}"
    
    def comments_count(self):
        return self.comments.count()
    
    def likes_count(self):
        return self.likes.count()
    

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')

    def __str__(self):
        return f"{self.user.username} likes {self.post}"


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author.username} - {self.content[:20]}"


