# bookshelf/forms.py
from django import forms
from bookshelf.models import Book, Author

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']

    # Optional: sanitize input to prevent XSS
    def clean_title(self):
        title = self.cleaned_data.get('title')
        # simple check to prevent HTML tags in title
        if '<' in title or '>' in title:
            raise forms.ValidationError("HTML tags are not allowed in book title.")
        return title

    # Optional: additional author validation
    def clean_author(self):
        author = self.cleaned_data.get('author')
        if author is None:
            raise forms.ValidationError("Please select a valid author.")
        return author
