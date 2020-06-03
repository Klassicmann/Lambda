from django import forms
from django.forms import ModelForm
from .models import Video


class VideosForm(ModelForm):
    class Meta:
        model = Video
        exclude = ('authur','subscribers',)