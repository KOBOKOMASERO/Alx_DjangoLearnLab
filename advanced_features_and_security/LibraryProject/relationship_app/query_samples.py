import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

author_name = 'J.K. Rowling'
library_name = 'Central Library'

try:
    author = Author.objects.get(name=author_name)
    books_by_author = Book.objects.filter(author=author)
    print(f"Books by {author_name}:")
    for book in books_by_author:
        print(f"- {book.title}")
except Author.DoesNotExist:
    print(f"No author found with name {author_name}")

print("\n" + "="*50 + "\n")

try:
    library = Library.objects.get(name=library_name)
    books_in_library = library.books.all()
    print(f"Books in {library_name}:")
    for book in books_in_library:
        print(f"- {book.title}")

    try:
        librarian = Librarian.objects.get(library=library)
        print(f"Librarian for {library_name}: {librarian.name}")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to {library_name}")

except Library.DoesNotExist:
    print(f"No library found with name {library_name}")
