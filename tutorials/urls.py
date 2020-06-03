from django.urls import path,include
from . import views as view
from rest_framework import routers
from tutorials.api import VideoViewSet

router = routers.DefaultRouter()
router.register('api/videos', VideoViewSet, 'tutorials' )

urlpatterns = [
    path('create', view.video_tutorial_create, name='create-video-tutorial'),
    path('list', view.VideoListView.as_view(), name='video-list'),
    path('<pk>', view.VideoDetailView.as_view(), name='video-detail'),
    
    path('', include(router.urls)),

]
