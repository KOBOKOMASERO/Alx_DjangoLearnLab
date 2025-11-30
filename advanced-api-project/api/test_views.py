from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Book, Author
from .serializers import BookSerializer

class BookAPITestCase(APITestCase):
    """
    Test suite for Book API endpoints:
    - CRUD operations
    - Filtering, searching, ordering
    - Permissions enforcement
    """

    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = APIClient()

        # Create authors
        self.author1 = Author.objects.create(name="Author One")
        self.author2 = Author.objects.create(name="Author Two")

        # Create books
        self.book1 = Book.objects.create(
            title="Book One",
            publication_year=2020,
            author=self.author1
        )
        self.book2 = Book.objects.create(
            title="Book Two",
            publication_year=2022,
            author=self.author2
        )

    # -------------------------
    # TEST LIST VIEW
    # -------------------------
    def test_list_books(self):
        """Ensure we can retrieve a list of books"""
        url = reverse('book-list')
        response = self.client.get(url)
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    # -------------------------
    # TEST CREATE VIEW
    # -------------------------
    def test_create_book_authenticated(self):
        """Authenticated user can create a book"""
        self.client.login(username='testuser', password='testpass')
        url = reverse('book-create')
        data = {
            'title': "New Book",
            'publication_year': 2023,
            'author': self.author1.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.last().title, "New Book")

    def test_create_book_unauthenticated(self):
        """Unauthenticated user cannot create a book"""
        url = reverse('book-create')
        data = {
            'title': "Unauthorized Book",
            'publication_year': 2023,
            'author': self.author1.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # -------------------------
    # TEST DETAIL VIEW
    # -------------------------
    def test_retrieve_book(self):
        """Retrieve a single book"""
        url = reverse('book-detail', kwargs={'pk': self.book1.id})
        response = self.client.get(url)
        serializer = BookSerializer(self.book1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    # -------------------------
    # TEST UPDATE VIEW
    # -------------------------
    def test_update_book_authenticated(self):
        """Authenticated user can update a book"""
        self.client.login(username='testuser', password='testpass')
        url = reverse('book-update', kwargs={'pk': self.book1.id})
        data = {
            'title': "Updated Book One",
            'publication_year': 2021,
            'author': self.author1.id
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Book One")

    def test_update_book_unauthenticated(self):
        """Unauthenticated user cannot update a book"""
        url = reverse('book-update', kwargs={'pk': self.book1.id})
        data = {
            'title': "Hacked Book",
            'publication_year': 2021,
            'author': self.author1.id
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # -------------------------
    # TEST DELETE VIEW
    # -------------------------
    def test_delete_book_authenticated(self):
        """Authenticated user can delete a book"""
        self.client.login(username='testuser', password='testpass')
        url = reverse('book-delete', kwargs={'pk': self.book2.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book2.id).exists())

    def test_delete_book_unauthenticated(self):
        """Unauthenticated user cannot delete a book"""
        url = reverse('book-delete', kwargs={'pk': self.book2.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # -------------------------
    # TEST FILTERING, SEARCHING, ORDERING
    # -------------------------
    def test_filter_books_by_author(self):
        """Filter books by author"""
        url = reverse('book-list') + f'?author={self.author1.id}'
        response = self.client.get(url)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author'], self.author1.id)

    def test_search_books_by_title(self):
        """Search books by title"""
        url = reverse('book-list') + '?search=Two'
        response = self.client.get(url)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Book Two")

    def test_order_books_by_publication_year(self):
        """Order books by publication_year descending"""
        url = reverse('book-list') + '?ordering=-publication_year'
        response = self.client.get(url)
        self.assertEqual(response.data[0]['publication_year'], 2022)
