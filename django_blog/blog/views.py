from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .models import Post, Profile
from .forms import CustomUserCreationForm, ProfileForm

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
    success_url = reverse_lazy('posts')


def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)

def post(self, request, *args, **kwargs):
    form = self.get_form()
    if form.is_valid():
        form.save()
        return self.form_valid(form)
    else:
        return self.form_invalid(form)
    

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('posts')


def test_func(self):
    post = self.get_object()
    return self.request.user == post.author

def post(self, request, *args, **kwargs):
    form = self.get_form()
    if form.is_valid():
        form.save()
        return self.form_valid(form)
    else:
        return self.form_invalid(form)


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('posts')


def test_func(self):
    post = self.get_object()
    return self.request.user == post.author

# ---------------------------

# Authentication Views

# ---------------------------

class RegisterView(CreateView):
    template_name = "blog/register.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")

def post(self, request, *args, **kwargs):
    form = self.get_form()
    if form.is_valid():
        form.save()
        return self.form_valid(form)
    else:
        return self.form_invalid(form)

class UserLoginView(LoginView):
    template_name = "blog/login.html"

class UserLogoutView(LogoutView):
    next_page = reverse_lazy("home")

class ProfileView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = "blog/profile.html"
    success_url = reverse_lazy("profile")


def get_object(self, queryset=None):
    return self.request.user.profile

def post(self, request, *args, **kwargs):
    form = self.get_form()
    if form.is_valid():
        form.save()
        return self.form_valid(form)
    else:
        return self.form_invalid(form)
