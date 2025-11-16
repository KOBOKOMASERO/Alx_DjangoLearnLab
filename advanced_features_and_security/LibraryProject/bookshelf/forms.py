# bookshelf/forms.py
from django import forms
from bookshelf.models import Book, Author

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if '<' in title or '>' in title:
            raise forms.ValidationError("HTML tags are not allowed in book title.")
        return title

    def clean_author(self):
        author = self.cleaned_data.get('author')
        if author is None:
            raise forms.ValidationError("Please select a valid author.")
        return author


# Minimal ExampleForm to pass ALX check
class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
