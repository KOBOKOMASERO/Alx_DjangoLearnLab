from django.urls import path
from .views import (
HomeView, PostListView, PostDetailView, PostCreateView,
PostUpdateView, PostDeleteView,
RegisterView, UserLoginView, UserLogoutView, ProfileView
)

urlpatterns = [
# Blog CRUD URLs
path('', HomeView.as_view(), name='home'),
path('posts/', PostListView.as_view(), name='posts'),
path('posts/new/', PostCreateView.as_view(), name='post_create'),
path('posts/[int:pk](int:pk)/', PostDetailView.as_view(), name='post_detail'),
path('posts/[int:pk](int:pk)/edit/', PostUpdateView.as_view(), name='post_update'),
path('posts/[int:pk](int:pk)/delete/', PostDeleteView.as_view(), name='post_delete'),


# Authentication URLs
path('register/', RegisterView.as_view(), name='register'),
path('login/', UserLoginView.as_view(), name='login'),
path('logout/', UserLogoutView.as_view(), name='logout'),
path('profile/', ProfileView.as_view(), name='profile'),
]
