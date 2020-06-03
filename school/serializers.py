from rest_framework import serializers
from .models import (
    School, Class, Student, Teacher, Fee
)

class SchoolSerializer(serializers.Serializer):
    class Meta:
        model = School
        fields='__all__'

class ClassSerializer(serializers.Serializer):
    class Meta:
        model = Class
        fields='__all__'

class StudentSerializer(serializers.Serializer):
    class Meta:
        model = Student
        fields='__all__'

class TeacherSerializer(serializers.Serializer):
    class Meta:
        model = Teacher
        fields='__all__'


class FeeSerializer(serializers.Serializer):
    class Meta:
        model = Fee
        fields='__all__'
