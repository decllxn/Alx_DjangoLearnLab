from django.shortcuts import render
from .models import Book

# The example the functions retreives all books and renders a template displaying the list

def book_list(request):
    books = Book.objects.all() # Fetch all book instances from the db
    context = {'book_list': books} # Create a context dictionary with the book list
    return render(request, 'books/book_list.html', context)
