from django.shortcuts import render
from relationship_app.models import Book

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # Fetch all books from the database
    return render(request, 'list_books.html', {'books': books})


from django.shortcuts import render
from django.views.generic import DetailView
from relationship_app.models import Library

# Class-based view for displaying library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'  # To access the library object in the template

