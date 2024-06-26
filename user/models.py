from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default-profile.jpg', upload_to='profile-pics')
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        image = Image.open(self.image.path) # get the image

        if image.width > 150 or image.height > 150:
            max_size = (150, 150) # sizing of max width and length 
            image.thumbnail(max_size)  # resizing image to max size
            image.save(self.image.path) # saving image