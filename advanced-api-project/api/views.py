from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    """
    BookListView:
    Retrieves all Book instances.
    - GET method
    - Accessible to anyone (read-only)
    - Uses BookSerializer to serialize data
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookDetailView(generics.RetrieveAPIView):
    """
    BookDetailView:
    Retrieves a single Book by primary key (id).
    - GET method
    - Accessible to anyone (read-only)
    - Uses BookSerializer to serialize data
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookCreateView(generics.CreateAPIView):
    """
    BookCreateView:
    Creates a new Book instance.
    - POST method
    - Requires authentication
    - Uses BookSerializer for input validation and serialization
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookUpdateView(generics.UpdateAPIView):
    """
    BookUpdateView:
    Updates an existing Book instance.
    - PUT/PATCH methods
    - Requires authentication
    - Book is identified by primary key in the URL or in the request data if customized
    - Uses BookSerializer for validation
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookDeleteView(generics.DestroyAPIView):
    """
    BookDeleteView:
    Deletes an existing Book instance.
    - DELETE method
    - Requires authentication
    - Book is identified by primary key in the URL or in the request data if customized
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
