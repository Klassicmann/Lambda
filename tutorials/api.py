from tutorials.serializers import VideoSerializer
from rest_framework import permissions, viewsets
from tutorials.models import Video

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()    
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = VideoSerializer