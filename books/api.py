from books.serializers import BookSerializer
from rest_framework import permissions, viewsets
from books.models import Book

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()    
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = BookSerializer