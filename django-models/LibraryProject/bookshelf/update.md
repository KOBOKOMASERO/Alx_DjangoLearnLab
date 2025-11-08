# Update Book

Open Django shell:

```bash
python manage.py shell

from bookshelf.models import Book

# Get the book
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()
book
# Expected output:
# <Book: Nineteen Eighty-Four>
