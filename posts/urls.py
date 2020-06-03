from django.urls import path
from . import views as view

urlpatterns = [
    path('', view.PostListView.as_view(), name='post-list'),
    path('<int:pk>', view.PostDetailView.as_view(), name='post-detail'),
    path('create', view.create_post, name='create-post'),
]

