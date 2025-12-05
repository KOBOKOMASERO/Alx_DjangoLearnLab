from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Comment, Tag, Post

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
    tags = forms.CharField(
        required=False,
        label="Tags (comma separated)",
        help_text="Example: django, python, web"
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

    def __init__(self, *args, **kwargs):
        instance = kwargs.get("instance")
        super().__init__(*args, **kwargs)
        if instance:
            self.fields["tags"].initial = ", ".join([t.name for t in instance.tags.all()])

    def clean_tags(self):
        raw = self.cleaned_data.get("tags", "")
        tags = [t.strip().lower() for t in raw.split(",") if t.strip()]
        return list(dict.fromkeys(tags))  # deduplicate while preserving order

    def save(self, commit=True):
        post = super().save(commit=False)
        if commit:
            post.save()

        # Handle tags
        tags = self.cleaned_data.get("tags", [])
        tag_objects = []

        for tag_name in tags:
            tag_obj, created = Tag.objects.get_or_create(name=tag_name)
            tag_objects.append(tag_obj)

        post.tags.set(tag_objects)
        return post
