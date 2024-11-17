from django.shortcuts import render
from django.views.generic import DetailView  # Import DetailView
from .models import Library  # Import Library model

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # Fetch all books from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view for displaying library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # Path to the template
    context_object_name = 'library'  # Name for the context variable in the template
