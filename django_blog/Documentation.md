# Django Blog Authentication System Documentation

## 1. Overview

The authentication system provides **user registration, login, logout, and profile management** for the Django blog project. It leverages Django’s built-in authentication system while adding custom functionality for registration and profile editing.

### Key Components

* **Registration:** Uses a custom form `CustomUserCreationForm` extending `UserCreationForm` to include an email field.
* **Login & Logout:** Managed using Django’s built-in `LoginView` and `LogoutView`.
* **Profile Management:** Authenticated users can view and update their username and email using `ProfileView`.

---

## 2. Setup Instructions

### 2.1 Install Requirements

Ensure your virtual environment is active and Django is installed:

```bash
pip install django
```

### 2.2 Add Authentication URLs

In `blog/urls.py`, include the following paths:

```python
from django.urls import path
from .views import RegisterView, UserLoginView, UserLogoutView, ProfileView

urlpatterns += [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
```

### 2.3 Create Custom User Form

In `forms.py`:

```python
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
```

### 2.4 Create Authentication Views

In `views.py`:

```python
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'blog/register.html'
    success_url = reverse_lazy('login')

class UserLoginView(LoginView):
    template_name = 'blog/login.html'

class UserLogoutView(LogoutView):
    next_page = 'home'

class ProfileView(UpdateView):
    model = User
    fields = ['username', 'email']
    template_name = 'blog/profile.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user
```

### 2.5 Create Templates

* `register.html` – Form for new users.
* `login.html` – Login form.
* `profile.html` – Profile update form.
* `logout.html` – Optional logout confirmation.
  Ensure templates use `{% csrf_token %}` in forms for security.

---

## 3. User Guide

### 3.1 Registration

* Navigate to `/register/`
* Fill in `username`, `email`, and password.
* On success, redirected to login page.

### 3.2 Login

* Navigate to `/login/`
* Enter credentials.
* On success, redirected to home page.

### 3.3 Logout

* Click the logout link.
* Redirected to home page.

### 3.4 Profile Management

* Navigate to `/profile/`
* Update username or email.
* Submit to save changes.

---

## 4. Security Notes

* **CSRF Protection:** All forms include `{% csrf_token %}`.
* **Password Storage:** Django handles hashing using `PBKDF2` by default.
* **Access Control:** `ProfileView` uses the logged-in user object to prevent editing other users’ profiles.
