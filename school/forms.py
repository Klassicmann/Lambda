from django import forms
from school.models import (
    School,
    Student,
    Teacher,
    
)
from django.forms import ModelForm


class SchoolForm(ModelForm):
    class Meta:
        model = School
        exclude = ('created_by',)


class StudentForm(ModelForm):
    class Meta:
        model = Student
        exclude = ('school',)


class TeachersForm(ModelForm):
    class Meta:
        model = Teacher
        exclude = ('school',)


        