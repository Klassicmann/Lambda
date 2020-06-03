from django.urls import path, include
from . import views as view
from rest_framework import routers
from books.api import BookViewSet


router = routers.DefaultRouter()
router.register('api/books', BookViewSet, 'books' )
urlpatterns = [
    path('', view.BookList.as_view(), name='book_list'),
    path('create', view.create_book, name='create_book'),
    path('<pk>', view.BookDetailView.as_view(), name='book-detail'),
    path('<pk>/update', view.BookUpdateView.as_view(), name='book-update'),
    path('<pk>/delete', view.BookDeleteView.as_view(), name='book-delete'),

    #API Paths
    path('', include(router.urls)),
   
]
 