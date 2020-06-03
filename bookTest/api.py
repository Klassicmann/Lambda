from .serializers import BookTestSerializer
from rest_framework import permissions, viewsets
from .models import BookTest

class BookViewSet(viewsets.ModelViewSet):
    queryset = BookTest.objects.all()    
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = BookTestSerializer