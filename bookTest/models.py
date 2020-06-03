from django.db import models
from django.contrib.auth.models import User

class BookTest(models.Model):
    posted_by = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    authur = models.CharField(max_length = 100, default = 'Anonymous')
    about_authur = models.TextField(default='Add book description')
    book_title = models.CharField(max_length=250)