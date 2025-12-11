from django.urls import path
from .views import RegisterAPIView, LoginAPIView, ProfileAPIView, PublicUserAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('profile/', ProfileAPIView.as_view(), name='profile'),
    path('users/<str:username>/', PublicUserAPIView.as_view(), name='public-user'),
]