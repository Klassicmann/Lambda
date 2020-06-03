from rest_framework.serializers import ModelSerializer
from tutorials.models import Video

class VideoSerializer(ModelSerializer):
    class Meta:
        model = Video
        fields='__all__'


