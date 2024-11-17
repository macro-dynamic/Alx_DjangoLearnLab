from relationship_app.models import Library, Librarian

# Retrieve the librarian for a specific library
def get_librarian_for_library(library_id):
    try:
        library = Library.objects.get(id=library_id)
        librarian = Librarian.objects.get(library=library)
        return librarian
    except Library.DoesNotExist:
        print("Library not found")
    except Librarian.DoesNotExist:
        print("No librarian assigned to this library")

# Example Usage: Retrieve librarian for library with ID 1
librarian = get_librarian_for_library(1)
if librarian:
    print(f"Librarian for library: {librarian.name}")
