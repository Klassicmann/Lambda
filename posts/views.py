from django.shortcuts import render
from django.views.generic import *
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Post
from django.contrib.auth.models import User
from .forms import PostForm


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'


@login_required
def create_post(request):
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        
        if form.is_valid():
            instance = form.save(commit=False)
            instance.authur = request.user
            form.save()

        return HttpResponseRedirect('/accounts/profile')

    else:

        form = PostForm()
    return render(request, 'posts/post_create.html', {'form': form})

    

