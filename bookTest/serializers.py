from rest_framework import serializers 
from .models import BookTest

class BookTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookTest
        fields='__all__'
