from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

# ============================
# BookSerializer
# ============================
# Serializes the Book model.
# - Includes all fields of the Book model.
# - Adds custom validation to make sure publication_year isn't in the future.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'   # Includes: title, publication_year, author

    # Custom field-level validation:
    # Ensures that the publication year is not greater than the current year.
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


# ============================
# AuthorSerializer
# ============================
# Serializes the Author model.
# - Includes the author's name.
# - Also includes a nested list of the author's books using BookSerializer.
# - The nested books are read-only (we don't create books through AuthorSerializer).
class AuthorSerializer(serializers.ModelSerializer):
    # Nested serializer:
    # Pulls all books related to this author using the related_name="books".
    # many=True → because an author can have multiple books.
    # read_only=True → prevents creating books from inside the AuthorSerializer.
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']  # Return author name + their books

        # The relationship handling:
        # Django looks at "related_name='books'" in the Book model and fetches:
        # all books where book.author == this author.
