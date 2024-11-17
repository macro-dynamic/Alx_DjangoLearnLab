from django.shortcuts import render
from django.views.generic.detail import DetailView  # Correct import for DetailView
from .models import Book, Library  # Ensure all models are imported

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # Fetch all books from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view for displaying library details
class LibraryDetailView(DetailView):
    model = Library  # Define the model for the view
    template_name = 'relationship_app/library_detail.html'  # Path to the template
    context_object_name = 'library'  # Name for the context variable in the template
