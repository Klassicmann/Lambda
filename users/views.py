from django.db.models import Q
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView, DeleteView, UpdateView
from .forms import UpdateProfileImgForm
from django.contrib.auth.models import User
from .models import Profile
from books.models import Book
from course.models import Course, CourseVideo, CourseDocument
from tutorials.models import Video
from posts.models import Post
from school.models import Student

@login_required
def profile(request):
    book_list = Book.objects.all().order_by('created_at')
    course_list = Course.objects.all().order_by('released_on')
    video_list = Video.objects.all().order_by('created_at')
    post_list = Post.objects.all().order_by('created_on')
    page = request.GET.get('page', 1)
    paginator = Paginator(book_list, 6)
    query = request.GET.get('q')
    if query:

        book_list = book_list.filter(Q(authur__icontains=query) |
                                     Q(book_title__icontains=query) |
                                     Q(book_type__icontains=query) |
                                     Q(level__icontains=query) |
                                     Q(departments__icontains=query)
                                     )

        video_list = video_list.filter(Q(authur__username__icontains=query) |
                                       Q(title__icontains=query)
                                       )

        course_list = course_list.filter(Q(title__icontains=query) |
                                         Q(authur__username__icontains=query)
                                         )

        post_list = post_list.filter(Q(title__icontains=query) |
                                 Q(authur__username__icontains=query) |
                                 Q(description__icontains=query)
                                 )

    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    if request.method == 'POST':
        form = UpdateProfileImgForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            request.user.profile.image = instance.image
            request.user.profile.save()
    else:
        form = UpdateProfileImgForm()

    template = 'users/profile.html'
    context = {
        'books': books,
        'course_list': course_list,
        'video_list': video_list,
        'post_list': post_list,
        'form': form,
    }
    return render(request, template, context)


@login_required
def update_profile_image(request):
    if request.method == 'POST':
        form = UpdateProfileImg(request.POST, request.FILES)

        if form.is_valid():
            instance = form.save(commit=False)
            request.user.profile.image = instance.image
            request.user.profile.save()

    else:
        form = UpdateProfileImg()
    return render(request, 'users/profile_create.html', {'form': form})


class Users(ListView):
    model = User
    template_name = 'users/users.html'
    context_object_name = 'users'


class UserDetailView(DetailView):
    model = User
    context_object_name = 'user'
    template_name = 'users/user_detail.html'


def forum(request):

    return render(request, 'scul/forum.html')