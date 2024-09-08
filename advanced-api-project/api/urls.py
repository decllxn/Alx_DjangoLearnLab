from django.urls import path
from .views import CreateView, UpdateView, DeleteView, ListView, DetailView

urlpatterns = [
    path('books/', ListView.as_view(), name='book-list'),  # URL for listing all books
    path('books/<int:pk>/', DetailView.as_view(), name='book-detail'),  # URL for retrieving a specific book
    path('books/create/', CreateView.as_view(), name='book-create'),  # URL for creating a new book
    path('books/update/', UpdateView.as_view(), name='book-update'),  # URL for updating a specific book
    path('books/delete/', DeleteView.as_view(), name='book-delete'),  # URL for deleting a specific book
]
