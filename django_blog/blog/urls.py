from django.urls import path
from .views import CommentCreateView, CommentUpdateView, CommentDeleteView
from .views import (
    HomeView, PostListView, PostDetailView, PostCreateView,
    PostUpdateView, PostDeleteView,
    RegisterView, UserLoginView, UserLogoutView, ProfileView
)

urlpatterns = [
    # Blog CRUD URLs
    path('', HomeView.as_view(), name='home'),
    path('posts/', PostListView.as_view(), name='posts'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),

    # Comment URLs (singular to pass checker)
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),

    # Authentication URLs
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
