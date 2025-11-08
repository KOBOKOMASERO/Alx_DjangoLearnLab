# Retrieve Book

Open Django shell:

```bash
python manage.py shell

from bookshelf.models import Book

# Retrieve all books
Book.objects.all()
# Expected output:
# <QuerySet [<Book: 1984>]>

# Retrieve a specific book
book = Book.objects.get(title="1984")
book.title, book.author, book.publication_year
# Expected output:
# ('1984', 'George Orwell', 1949)
