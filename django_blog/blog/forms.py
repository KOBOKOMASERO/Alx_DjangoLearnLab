from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from taggit.forms import TagWidget  # ← REQUIRED
from .models import Profile, Comment, Post


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("bio", "avatar")


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), label='')
    class Meta:
        model = Comment
        fields = ['content']


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

        # REQUIRED FOR THE TASK
        widgets = {
            'tags': TagWidget(),   # ← REQUIRED
        }
