# bookshelf/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_books, name='list_books'),
    path('add/', views.add_book, name='add_book'),
    path('<int:pk>/edit/', views.edit_book, name='edit_book'),
    path('<int:pk>/delete/', views.delete_book, name='delete_book'),
    path('example/', views.example_form_view, name='example_form'),  
]
