from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    """
    BookListView:
    Retrieves all Book instances.
    - GET method
    - Accessible to anyone (read-only)
    - Supports filtering, searching, and ordering
    Filtering: title, author, publication_year
    Searching: title, author
    Ordering: title, publication_year
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Enable filtering, searching, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year']   # filtering
    search_fields = ['title', 'author__name']                    # searching
    ordering_fields = ['title', 'publication_year']             # ordering
    ordering = ['title']  # default ordering

class BookDetailView(generics.RetrieveAPIView):
    """
    BookDetailView:
    Retrieves a single Book by primary key (id).
    - GET method
    - Accessible to anyone
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
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
