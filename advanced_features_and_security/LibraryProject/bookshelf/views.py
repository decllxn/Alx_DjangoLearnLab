from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from django.contrib.auth import login as auth_login, authenticate
from django.contrib import messages
from .models import Book
from .forms import BookForm
from .forms import SearchForm
from .forms import ExampleForm


# Create your views here.
@permission_required('bookshelf.can_view', raise_exception=True)
def view_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(request, 'bookshelf/book_detail.html', {'book': book})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book created successfully')
            return redirect('book_list')
    else:
        form = BookForm()

    return render(request, 'bookshelf/book_form.html', {'form': form})

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book updated successfully')
            return redirect('book_detail', book_id=book.id)  # Replace with the name of your book detail view
    else:
        form = BookForm(instance=book)

    return render(request, 'bookshelf/book_form.html', {'form': form})


@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        book.delete()
        messages.success(request, 'Book deleted successfully')
        return redirect('book_list')  # Replace with the name of your book list view

    return render(request, 'bookshelf/book_confirm_delete.html', {'book': book})

def custom_permission_denied_view(request, exception):
    return render(request, '403.html', status=403)

def book_list(request):
    # Handle form submission if POST request
    form  = SearchForm(request.POST or None)
    book = Book.objects.all()


    if request.method == 'POST' and form.is_valid():
        search_query = form.cleaned_data['search']
        if search_query:
            books = books.filter(title__icontains=search_query) | books.filter(author__icontains=search_query)

    context = {
        'form': form,
        'books': books
    }
    return render(request, 'book_list.html', context)