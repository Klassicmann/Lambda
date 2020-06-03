from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from course.models import Course, CourseVideo, CourseDocument
from .forms import CourseForm, CourseVideoForm, CourseDocumentForm


class CourseDetailView(DetailView):
    
    model = Course
    context_object_name = 'course'
    template_name = 'courses/course_detail.html'

    def get_context_data(self, **kwargs):
           context = super(CourseDetailView, self).get_context_data(**kwargs)
        
           course = Course.objects.values_list('title', flat = True).get(id = self.object.pk)
           videos = CourseVideo.objects.filter(course__title = course)
           vid = CourseVideo.objects.filter(course__title = course).first()
           documents = CourseDocument.objects.filter(video__video_title = vid.video_title)

           context.update({
           'videos': videos,
           'vid':vid,
           'documents': documents,
           })
           return context

class CourseListView(ListView):
    
    model = Course
    context_object_name = 'courses'
    template_name = 'courses/course_list.html'


@login_required
def create_course(request):

    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            course = form.save(commit=False)
            course.authur = request.user
            course.save()

        return HttpResponseRedirect('/courses/add-videos')

    else:

        form = CourseForm()
    return render(request, 'courses/course_create.html', {'form': form})


@login_required
def create_course_video(request):

    if request.method == 'POST':
        form = CourseVideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

        return HttpResponseRedirect('/courses/add-documents')

    else:

        form = CourseVideoForm()
    return render(request, 'courses/coursevideo_create.html', {'form': form})


class CourseDocumentsCreate(CreateView):
    model = CourseDocument
    fields = '__all__'
    template_name = 'courses/coursedocument_create.html'
    success_url = reverse_lazy('profile')


