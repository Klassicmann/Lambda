from django.contrib import admin
from .models import School, Class, Student, Teacher, Fee, Payment

admin.site.register([School, Class, Student, Teacher, Fee, Payment])
