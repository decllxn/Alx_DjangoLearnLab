# Django Admin Configuration for Book Model

## Steps Taken:

1. **Registered the `Book` Model:**
   - Added `Book` model to `bookshelf/admin.py`.

   ```python
   from django.contrib import admin
   from .models import Book

   @admin.register(Book)
   class BookAdmin(admin.ModelAdmin):
       list_display = ('title', 'author', 'publication_year')
       list_filter = ('author', 'publication_year')
       search_fields = ('title', 'author')

