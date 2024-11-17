# query_samples.py
import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')  # Replace with your project name
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    # Use filter to get all books by a specific author
    books = Book.objects.filter(author__name=author_name)
    if books.exists():
        print(f"Books by {author_name}: {[book.title for book in books]}")
    else:
        print(f"No books found for author {author_name}.")

def list_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"Books in {library_name}: {[book.title for book in books]}")
    except Library.DoesNotExist:
        print(f"Library {library_name} does not exist.")

def retrieve_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian
        print(f"Librarian for {library_name}: {librarian.name}")
    except Library.DoesNotExist:
        print(f"Library {library_name} does not exist.")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to {library_name}.")

# Sample usage
if __name__ == "__main__":
    query_books_by_author('J.K. Rowling')  # Replace with an actual author name in your database
    list_books_in_library('Central Library')  # Replace with an actual library name in your database
    retrieve_librarian_for_library('Central Library')  # Replace with an actual library name in your database
