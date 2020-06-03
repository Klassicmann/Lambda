from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import VideosForm
from .models import Video


@login_required
def video_tutorial_create(request):
    if request.method == 'POST':
        form = VideosForm(request.POST, request.FILES)

        if form.is_valid():
            tuto = form.save(commit=False)
            tuto.authur = request.user
            tuto.save()

        return HttpResponseRedirect('/accounts/profile')

    else:

        form = VideosForm()
    return render(request, 'videos/video_create.html', {'form': form})


class VideoListView(ListView):
    model = Video
    template_name = 'videos/video_list.html'
    context_object_name = 'videos'


class VideoDetailView(DetailView):
    model = Video
    context_object_name = 'video'
    template_name = 'videos/video_detail.html'

    def get_context_data(self, **kwargs):
        context = super(VideoDetailView, self).get_context_data(**kwargs)
        other_videos = Video.objects.all()
        context.update({
            'other_videos': other_videos
        })
        return context
