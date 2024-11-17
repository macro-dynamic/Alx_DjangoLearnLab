from django.shortcuts import render
from django.views.generic.detail import DetailView  # Correct import for DetailView
from .models import Book, Library  # Ensure that Book and Library models are correctly imported

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # Fetch all books from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view for displaying library details
class LibraryDetailView(DetailView):
    model = Library  # Specify the model for this view
    template_name = 'relationship_app/library_detail.html'  # Template for the class-based view
    context_object_name = 'library'  # This is the context variable that will be available in the template

    def get_context_data(self, **kwargs):
        """
        Adds books related to this library to the context data.
        """
        context = super().get_context_data(**kwargs)  # Get the default context from the parent class
        context['books'] = self.object.books.all()  # Add books related to the specific library to the context
        return context
