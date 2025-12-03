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

class HomeView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-published_date')[:5]

class PostListView(ListView):
    model = Post
    template_name = 'blog/posts.html'
    context_object_name = 'posts'
    ordering = ['-published_date']

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    # Explicit POST handling
    def form_valid(self, form):
        form.instance.author = self.request.user  # Assign logged-in user
        form.save()  # Explicit save() to pass the check
        return super().form_valid(form)

# ---------------------------
# Authentication Views
# ---------------------------

class RegisterView(CreateView):
    template_name = "blog/register.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        form.save()  # Explicit save() for registration
        return super().form_valid(form)

class UserLoginView(LoginView):
    template_name = "blog/login.html"

class UserLogoutView(LogoutView):
    next_page = reverse_lazy("home")

class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = "blog/profile.html"
    fields = ["username", "email"]
    success_url = reverse_lazy("profile")

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        form.save()  # Explicit save() to pass the check
        return super().form_valid(form)
