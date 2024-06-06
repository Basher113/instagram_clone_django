from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from PIL import Image

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.ImageField(upload_to='posts-content')
    caption = models.TextField(blank=True)
    date_posted = models.DateField(default=datetime.now, blank=True, null=True)

    def __str__(self):
        return f"POST: {self.id},  Author: {self.author}"
    
