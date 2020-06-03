from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill


class Post(models.Model):
    authur = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250, default='title')
    image = ProcessedImageField(default=None, upload_to='users/profile_images', processors=[ResizeToFill(700, 600)],
                                format='JPEG', options={'quality': 95}, blank=True, null=True)
    description = models.TextField(default='add description')
    created_on = models.DateField(auto_now=True)


    def __str__(self):
        return self.title
    
