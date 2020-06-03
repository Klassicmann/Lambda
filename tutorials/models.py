from django.db import models
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill
from django.contrib.auth.models import User

class Video(models.Model):
    authur = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    title = models.CharField(max_length=250)
    thumbnail= ProcessedImageField(default='default.png', upload_to='tutorials/videos', processors=[ResizeToFill(300, 200)],
                                        format='JPEG', options={'quality': 95})
    video = models.TextField()
    video_description = models.TextField()
    video_documents= models.FileField(upload_to = 'video_tutorials/documents', max_length = 250)
    price = models.IntegerField()
    subscribers = models.IntegerField(default=0)
    created_at = models.DateField(auto_now=True )

    def __str__(self):
        return self.title
