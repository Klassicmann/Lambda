from django.db import models
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill
from django.contrib.auth.models import User


CLASSES_CHOICES = [
    ('SS', 'Secondary Schools'),
    ('HS', 'High School'),
    ('U', 'University')
]
DEPARTMENT_CHOICES = [
    ('SS', 'Secondary School Science'),
    ('SA', 'Secondary School Art')

]
BOOK_TYPE_CHOICES = [
    ('PP', 'Past Papers'),
    ('TB', 'Text Book'),
    ('EZ', 'Examination Results'),
    ('SE', 'Solved Exercices'),
]


class Book(models.Model):
    posted_by = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    authur = models.CharField(max_length = 100, default = 'Anonymous')
    authur_image = ProcessedImageField(default='default.png', upload_to='books/authur_images', processors=[ResizeToFill(700, 600)],
                                       format='JPEG', options={'quality': 95})

    about_authur = models.TextField(default='Add book description')
    book_title = models.CharField(max_length=250)
    book_type = models.CharField(
        choices=BOOK_TYPE_CHOICES, max_length=2)
    level = models.CharField(choices=CLASSES_CHOICES, max_length=2)
    departments = models.CharField(choices=DEPARTMENT_CHOICES, max_length=2)
    price = models.IntegerField(default=0)
    file = models.FileField(upload_to='books/files', max_length=250)
    book_front_cover = ProcessedImageField(default='default.png', upload_to='books/images', processors=[ResizeToFill(500, 400)],
                                           format='JPEG', options={'quality': 95})

    book_back_cover = ProcessedImageField(default='default.png', upload_to='books/images', processors=[ResizeToFill(500, 400)],
                                          format='JPEG', options={'quality': 95})
    description = models.TextField(default='Add book description')
   
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.book_title
