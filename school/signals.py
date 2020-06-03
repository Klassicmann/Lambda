from django.db.models.signal import post_save
from django.contrib.auth.models import User
from django.dispatch import reciever
from .models import School


@erciever(post_save, sender=School)
def create_school(sender, instance, created, **kwargs):
    if created:
        School.obejects.create(created_by=instance)


@reciever(post_save, sender=School)
def save_school(sender, instance, **kwargs):
    instance.school.save()
