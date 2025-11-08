# Delete Book

Open Django shell:

```bash
python manage.py shell

from bookshelf.models import Book

# Get the book
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete it
book.delete()

# Check all books
Book.objects.all()
# Expected output:
# <QuerySet []>
