from django.dispatch import receiver
from allauth.account.signals import user_signed_up
from django.db.models.signals import post_save
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill
from django.db import models
from django.contrib.auth.models import User
from django.core.cache import cache
import datetime
from Lambda import settings
from school.models import School



ACCOUNT_TYPE_CHOICES = [
    ('Student', 'Student'),
    ('Teacher', 'Teacher'),
    ('Bookseller', 'Bookseller')
]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(default='', null=True, max_length=150)
    account_type = models.CharField(
        choices=ACCOUNT_TYPE_CHOICES, max_length=20)
    image = ProcessedImageField(default='default.png', upload_to='users/profile_images', processors=[ResizeToFill(300, 200)],
                                format='JPEG', options={'quality': 95}, blank=False, null=False)
    quater = models.CharField(blank=True, null=True, max_length=250)
    town = models.CharField(blank=True, null=True, max_length=250)
    school = models.ForeignKey(
        School, blank=True, null=True, on_delete=models.SET_NULL)
    likes = models.IntegerField(default=0)
    subscribers = models.IntegerField(default=0)

    def __str__(self):
        return "%s's profile" % self.user

    def last_seen(self):
        return cache.get('seen_%s' % self.user.username)

    def online(self):
        if self.last_seen():
            now = datetime.datetime.now()
            if now > self.last_seen() + datetime.timedelta(
                    seconds=settings.USER_ONLINE_TIMEOUT):
                return False
            else:
                return True
        else:
            return False

@receiver(post_save, sender=User)
def create_profile(sender, **kwargs):
    if kwargs.get('created', False):
        Profile.objects.create(user=kwargs['instance'])
