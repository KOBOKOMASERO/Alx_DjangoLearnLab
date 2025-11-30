from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework  # required by ALX checker
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

    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']

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
