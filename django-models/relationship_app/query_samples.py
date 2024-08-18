from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        return books
    except Author.DoesNotExist:
        return None

# List all books in a library
def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        return books
    except Library.DoesNotExist:
        return None

# Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        return librarian
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None

# Example usage
if __name__ == "__main__":
    # Replace 'Author Name' and 'Library Name' with actual data from your database
    author_books = get_books_by_author("Author Name")
    if author_books is not None:
        print(f"Books by Author: {[book.title for book in author_books]}")
    else:
        print("Author not found.")

    library_books = get_books_in_library("Library Name")
    if library_books is not None:
        print(f"Books in Library: {[book.title for book in library_books]}")
    else:
        print("Library not found.")

    librarian = get_librarian_for_library("Library Name")
    if librarian is not None:
        print(f"Librarian: {librarian.name}")
    else:
        print("Library or Librarian not found.")

