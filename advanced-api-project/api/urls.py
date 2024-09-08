from django.urls import path
from .views import CreateView, UpdateView, DeleteView

urlpatterns = [
    path('books/create/', CreateView.as_view(), name='book-create'),  # URL for creating a new book
    path('books/<int:pk>/update/', UpdateView.as_view(), name='book-update'),  # URL for updating a specific book
    path('books/<int:pk>/delete/', DeleteView.as_view(), name='book-delete'),  # URL for deleting a specific book
]
