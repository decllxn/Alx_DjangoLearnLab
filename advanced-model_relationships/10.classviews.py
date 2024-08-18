# The below example shows BookUpdateView that inherits from UpdateView and
# Facilitates updating details of a book. It defines the editable fields
# (title, author, description) and the template used for the update form

from django.views.generic import DetailView, UpdateView
from django.urls import reverse_lazy
from .models import Book

class BookUpdateView(UpdateView):
    # A class-based view for updating details of a specific book
    model = Book
    fields = ['title', 'author', 'description'] # Specify fields to be editable
    template_name = 'books/book_update_form.html'
    success_url = reverse_lazy('book_list') # URL to redirect after successful update

    def form_valid(self, form):
        # Executes custom logic after form validation
        response = super().form_valid(form) # Call defult form validation
