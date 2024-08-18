from django.views.generic import DetailView
from .models import Book

# A class-based view for displaying details of a specific book
class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'

    # Injects additional context data specific to the book
    def get_context_data(self, **kwargs):
        context = super().get_conext_data(**kwargs) # Get default context data
        book = self.get_object() # Retrieve the current book instance
        context['average_rating'] = book.get_average_rating()


