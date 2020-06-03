from django import forms
from django.forms import ModelForm
from .models import Course, CourseDocument, CourseVideo


class CourseForm(ModelForm):
    class Meta:
        model = Course
        exclude = ('authur',)


class CourseDocumentForm(ModelForm):
    class Meta:
        model = CourseDocument
        fields = '__all__'


class CourseVideoForm(ModelForm):
    class Meta:
        model = CourseVideo
        fields = '__all__'

