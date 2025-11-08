# CRUD Operations for Book Model

This document demonstrates all CRUD operations (Create, Retrieve, Update, Delete) for the `Book` model in the `bookshelf` app using Django's ORM.

Open Django shell:

```bash
python manage.py shell


from bookshelf.models import Book

# Create a new book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
# Expected output:
# <Book: 1984>

# Retrieve all books
Book.objects.all()
# Expected output:
# <QuerySet [<Book: 1984>]>

# Retrieve a specific book
book = Book.objects.get(title="1984")
book.title, book.author, book.publication_year
# Expected output:
# ('1984', 'George Orwell', 1949)

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()
book
# Expected output:
# <Book: Nineteen Eighty-Four>

# Delete the book
book.delete()

# Verify deletion
Book.objects.all()
# Expected output:
# <QuerySet []>
