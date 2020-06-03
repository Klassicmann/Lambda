from django.db import models

from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill
from django.urls import reverse

from django.contrib.auth.models import User



SCHOOL_CHOICES = [
    ('Primary school', 'Primary school'),
    ('Secondary School', 'Secondary School'),
    ('Pofessional School', 'Professional School'),
    ('University', 'University'),
    ('Evening School', 'Evening School')
]
STATUS_CHOICES = [
    ('Good', 'good'),
    ('Bad', 'Bad'),
    ('Critical', 'Critical'),
    
]

class School(models.Model):
    created_by = models.OneToOneField(User, on_delete = models.CASCADE, null= True, default = None)
    school_name = models.CharField(max_length=250, unique = True)
    registered_id = models.IntegerField()
    region = models.CharField(max_length=250)
    division = models.CharField(max_length=250)
    sub_division = models.CharField(max_length=250)
    town = models.CharField(max_length=250)
    quater = models.CharField(max_length=250)
    creation_date = models.DateField(max_length=250)
    school_type = models.CharField(choices=SCHOOL_CHOICES, max_length=100)
    status = models.CharField(choices = STATUS_CHOICES, max_length = 100, default='Good')

    logo = ProcessedImageField(default='default.png', upload_to='school/logo', processors=[ResizeToFill(500, 400)],
                               format='JPEG', options={'quality': 95})

    description = models.TextField()
    email = models.EmailField(max_length=254, default='example@school.com')
    created_at = models.DateField(auto_now=True)

    image_thumbnail = ImageSpecField(source='logo', processors=[
                                     ResizeToFill(150, 150)], format='JPEG', options={'quality': 60})

    def __str__(self):
        return self.school_name
    


class Class(models.Model):
    school = models.ForeignKey(School, on_delete = models.CASCADE)
    name = models.CharField(max_length=100, unique = True)

    class Meta:
        verbose_name = ("Class")
        verbose_name_plural =("Classes")

    def __str__(self):
        return self.name

GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Femail')
]
SPECIALITY_CHOICES = [
    ('Secondary School Science', 'Secondary School Science'),
    ('Secondary School Art ', 'Secondary School Art'),
    ('Marketing','Marketing'),
    ('Accountancy', 'Accountancy'),
    ('Transport and Logistics', 'Transport and Logistics'),
    ('Computer Engineering', 'Computer Engineering'),
    ('Telecommunication', 'Telecommunication')

] 


class Student(models.Model):
    school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True)
    student_class = models.ForeignKey(Class, on_delete = models.SET_NULL, null = True, default = 'no_class', related_name = 'student class')
    name = models.CharField(max_length=200, unique = True)
    student_class = models.ForeignKey(Class, on_delete=models.SET_NULL, null = True)
    address = models.CharField(max_length=200)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1)
    date_of_birth = models.DateField(auto_now=False)
    place_of_birth = models.CharField(max_length=100)
    students_phone = models.IntegerField()
    matricule = models.CharField(max_length=100)
    department = models.CharField(choices=SPECIALITY_CHOICES, max_length=100)
    student_image = ProcessedImageField(default='default.png', upload_to='student/images', processors=[ResizeToFill(500, 400)],
                                        format='JPEG', options={'quality': 95})
    

    def __str__(self):
        return self.name


class Teacher(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, unique = True) 
    teacher_class = models.ForeignKey(Class, default='teachers_class', on_delete= models.SET_NULL, null = True)
    address = models.CharField(max_length=200)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1)
    date_of_birth = models.DateField(auto_now=False)
    place_of_birth = models.CharField(max_length=100)
    teachers_phone = models.IntegerField()
    matricule = models.CharField(max_length=100)
    department = models.CharField(choices=SPECIALITY_CHOICES, max_length=100)
    teachers_image = ProcessedImageField(default='default.png', upload_to='student/images', processors=[ResizeToFill(700, 600)],
                                         format='JPEG', options={'quality': 95})

    def __str__(self):
        return self.name


class Fee(models.Model):
    name = models.CharField(max_length=250, null=True)
    amount = models.IntegerField()
    class_for_fees = models.ForeignKey(
        Class, related_name ='fees', null=True, default='All classes', on_delete=models.CASCADE)
    school = models.ForeignKey(School, default='no_school',
                               related_name='fees_for_school', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Payment(models.Model):
    teacher = models.ForeignKey(
        Teacher, null=True, default='teacher paymens', related_name='Payment', on_delete=models.CASCADE)
    amount = models.IntegerField()
    month = models.CharField(max_length = 50)

    def __str__(self):
        return self.month
