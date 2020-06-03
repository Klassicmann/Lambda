from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.views.generic import DetailView, ListView
from allauth.account.forms import SignupForm
from time import sleep
from .models import (School, Student, Class, Teacher)
from .forms import (SchoolForm, StudentForm, TeachersForm)


def home(request):
    template = 'scul/home.html'
    return render(request, template)


@login_required
def schools(request):
    sculs = School.objects.all()
    template = 'scul/school_list.html'
    query = request.GET.get('q')
    if query:

        sculs = sculs.filter(Q(school_name__icontains=query) |
                             Q(region__icontains=query) |
                             Q(division__icontains=query) |
                             Q(sub_division__icontains=query) |
                             Q(school_type__icontains=query) |
                             Q(town__icontains=query) |
                             Q(quater__icontains=query)
                             )

    return render(request, template, {'sculs': sculs})


class SchoolDetailView(DetailView):
    model = School
    template_name = 'scul/school_detail.html'


def school_detail(request, id):
    school = School.objects.get(id=School.id)
    return render(request, 'scul/school_list.html', {'school': school})


@login_required
def get_school(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SchoolForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            instance = form.save(commit=False)
            instance.created_by = request.user
            instance.save()

            return HttpResponseRedirect('/schools/')

    # if a GET (or any other method) we'll create a blank form
    else:

        form = SchoolForm()
    return render(request, 'scul/register_school.html', {'form': form})


class SchooolStudents(DetailView):
    model = School
    context_object_name = 'school'
    template_name = 'scul/students/student.html'

    def get_context_data(self, **kwargs):
        context = super(SchooolStudents, self).get_context_data(**kwargs)
        school = School.objects.values_list('school_name', flat = True).get(id = self.object.pk)
        classes = Class.objects.filter(school__school_name = school)

        students = Student.objects.filter(school__school_name = school)
        students = students.order_by('name')

        teachers = Teacher.objects.filter(school__school_name = school)
        teachers = teachers.order_by('name')

        get_class = self.request.GET.get('class')
        if get_class:
            students = Student.objects.filter(student_class__name = get_class)

        
        query = self.request.GET.get('q')
        if query:
            students = students.filter( Q(name__icontains=query) |
                                        Q(student_class__name__icontains=query)|
                                        Q(address__icontains=query) |
                                        Q(gender__icontains=query) |
                                        Q(matricule__icontains=query) |
                                        Q(department__icontains=query) 
                                        )

        context.update({
            'classes':classes,
            'students': students
        })

        return context


class SchooolTeachers(DetailView):
    model = School
    context_object_name = 'school'
    template_name = 'scul/teachers/teacher_list.html'
    def get_context_data(self, **kwargs):
        context = super(SchooolTeachers, self).get_context_data(**kwargs)
        school = School.objects.values_list('school_name', flat = True).get(id = self.object.pk)
        classes = Class.objects.filter(school__school_name = school)

        teachers = Teacher.objects.filter(school__school_name = school)
        teachers = teachers.order_by('name')

        get_class = self.request.GET.get('class')
        if get_class:
            teachers = Teacher.objects.filter(teacher_class__name = get_class)

        
        query = self.request.GET.get('q')
        if query:
            teachers = teachers.filter( Q(name__icontains=query) |
                                        Q(teacher_class__name__icontains=query)|
                                        Q(address__icontains=query) |
                                        Q(gender__icontains=query) |
                                        Q(matricule__icontains=query) |
                                        Q(department__icontains=query) 
                                        )

        context.update({
            'classes':classes,
            'teachers': teachers
        })

        return context


@login_required
def student_add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.school = request.user.school
            instance.name.capitalize()
            instance.save()
            return HttpResponseRedirect('/schools/')

    else:

        form = StudentForm()

    return render(request, 'scul/students/students_create.html', {'form': form})

@login_required
def teacher_add(request):
    if request.method == 'POST':
        form = TeachersForm(request.POST, request.FILES)
      
        if form.is_valid():
            instance = form.save(commit=False)
            instance.school = request.user.school
            instance.name.capitalize()
            instance.save()
            return HttpResponseRedirect('/schools')

    else:

        form = TeachersForm()

    return render(request, 'scul/teachers/teacher_create.html', {'form': form})


class StudentDetail(DetailView):
    model = Student
    context_object_name = 'student'
    template_name = 'scul/students/student-detail.html'


class TeacherDetail(DetailView):
    model = Teacher
    context_object_name = 'teacher'
    template_name = 'scul/teachers/teacher_detail.html'
