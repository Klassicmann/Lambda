from embed_video.fields import EmbedVideoField
from django.db import models
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill
from django.contrib.auth.models import User

class Course(models.Model):
    authur = models.ForeignKey(User,on_delete = models.SET_NULL, null=True)
    title = models.CharField(max_length=250)
    cover_picture = ProcessedImageField(default='default.png', upload_to='course/images', processors=[ResizeToFill(500, 400)],
                                        format='JPEG', options={'quality': 95})
    course_description = models.TextField()
    course_price = models.IntegerField()
    released_on = models.DateField(auto_now=True )

    def __str__(self):
        return self.title



class CourseVideo(models.Model):
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null = True)
    video_title = models.CharField(max_length = 200)
    video = models.TextField( default = 'Null')
    video_description = models.TextField()
    created_at = models.DateField(auto_now =True)

    def __str__(self):
        return self.video_title


class CourseDocument(models.Model):

    course = models.ForeignKey(
        Course, on_delete=models.CASCADE,  null=True, related_name='course_document')
    video = models.ForeignKey(CourseVideo, on_delete=models.SET_NULL, null=True, related_name='document_video')
    document_name = models.CharField(max_length = 250)
    created_at = models.DateField(auto_now=True )
    course_files = models.FileField( upload_to='course/course_files', max_length=250, null= True)

    def __str__(self):
        return self.document_name

