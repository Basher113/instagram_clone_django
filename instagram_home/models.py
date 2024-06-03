from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.ImageField(upload_to='posts-content')
    caption = models.TextField()

    def __str__(self):
        return f"POST: {self.id},  Author: {self.author}"
