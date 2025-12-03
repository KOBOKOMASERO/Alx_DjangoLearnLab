from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .models import Post
from .forms import CustomUserCreationForm

# ---------------------------
# Blog Views
# ---------------------------

# Home page - latest 5 posts
class HomeView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-published_date')[:5]

# All posts page
class PostListView(ListView):
    model = Post
    template_name = 'blog/posts.html'
    context_object_name = 'posts'
    ordering = ['-published_date']

# Single post page
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

# Create post page
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

# ---------------------------
# Authentication Views
# ---------------------------

# User registration
class RegisterView(CreateView):
    template_name = "blog/register.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")

# User login
class UserLoginView(LoginView):
    template_name = "blog/login.html"

# User logout
class UserLogoutView(LogoutView):
    next_page = reverse_lazy("home")

# User profile (view & update)
class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = "blog/profile.html"
    fields = ["username", "email"]
    success_url = reverse_lazy("profile")

    def get_object(self, queryset=None):
        return self.request.user
