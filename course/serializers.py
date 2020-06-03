from rest_framework import serializers
from .models import (
    Course, CourseVideo, CourseDocument
)

class CourseSerializer(serializers.Serializer):
    class Meta:
        model = Course
        fields='__all__'

class CourseVideoSerializer(serializers.Serializer):
    class Meta:
        model = CourseVideo
        fields='__all__'

class CourseDocumentSerializer(serializers.Serializer):
    class Meta:
        model = CourseDocument
        fields='__all__'
