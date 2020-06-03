from .forms import BookForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from time import sleep
from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, UpdateView
from .models import Book
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

#Serializer API

from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BookSerializer




class BookList(ListView):
    model = Book
    paginate_by = 6
    context_object_name = 'books'


@login_required
def create_book(request):

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            book = form.save(commit=False)
            book.posted_by = request.user
            book.save()

        return HttpResponseRedirect('/books/')

    else:

        form = BookForm()
    return render(request, 'books/create_book.html', {'form': form})


class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'


class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Book
    fields = '__all__'
    template_name = 'books/create_book.html'

    def test_func(self):
        book = self.get_object()
        if self.request.user == book.posted_by:
            return True
        return False


class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Book
    success_url = reverse_lazy('book_list')



#API Viesets

@api_view(["GET"])
class BooksView(APIView):

    # def get_object(self):
    #     try:
    #         return Book.objects.all()
    #     except Book.DoesNotExist:
    #         raise status.HTTP_404_NOT_FOUND

    def get(self, request, format=None):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
      
        return Response(data=serializer.data, status=status.HTTP_200_OK)


