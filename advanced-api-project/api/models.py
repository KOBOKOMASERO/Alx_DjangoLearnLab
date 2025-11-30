from django.db import models

# ============================
# Author Model
# ============================
# This model stores information about an author.
# Each author can have multiple books linked to them (one-to-many relationship).
class Author(models.Model):
    # Stores the author's full name.
    name = models.CharField(max_length=255)

    def __str__(self):
        # This helps display the author name in Django admin or shell.
        return self.name


# ============================
# Book Model
# ============================
# This model represents a book written by an author.
# Each book has a title, a publication year, and a reference to a specific Author.
class Book(models.Model):
    # Title of the book.
    title = models.CharField(max_length=255)

    # Year the book was published.
    publication_year = models.IntegerField()

    # ForeignKey creates a one-to-many relationship:
    # One author can have many books, but a book belongs to only one author.
    # related_name='books' allows access like: author.books.all()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        # Useful for admin and debugging.
        return f"{self.title} ({self.publication_year})"
