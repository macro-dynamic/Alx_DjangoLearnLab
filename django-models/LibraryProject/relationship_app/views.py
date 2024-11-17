from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView  # Import DetailView for class-based views
from .models import Book, Library  # Import both Book and Library models

# Function-based view to list all books with enhanced error handling
def list_books(request):
    try:
        # Fetch all books from the database
        books = Book.objects.all()  
        if not books:
            # Optionally handle the case where no books are found
            books_message = "No books found in the database."
            return render(request, 'relationship_app/list_books.html', {'books': books, 'books_message': books_message})
        return render(request, 'relationship_app/list_books.html', {'books': books})
    except Exception as e:
        # Basic error handling in case something goes wrong
        return render(request, 'relationship_app/list_books.html', {'error_message': f"Error: {str(e)}"})

# Class-based view to display details of a specific library, listing all books available
class LibraryDetailView(DetailView):
    model = Library  # The model we are working with
    template_name = 'relationship_app/library_detail.html'  # Specify the template for the view
    context_object_name = 'library'  # Variable name in the template for the library object

    def get_context_data(self, **kwargs):
        """
        Customize the context data to include additional information, such as a list of books
        available in this particular library.
        """
        context = super().get_context_data(**kwargs)  # Get the default context from the parent class
        context['books'] = self.object.books.all()  # Add books available in this library to the context
        return context
