from django import forms

from library.library_app.models import Book


class BookFormBase(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class CreateBookForm(BookFormBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = 'Title'
        self.fields['description'].widget.attrs['placeholder'] = 'Description'
        self.fields['image'].widget.attrs['placeholder'] = 'Image'
        self.fields['type'].widget.attrs['placeholder'] = 'Fiction, Novel, Crime..'


class EditBookForm(BookFormBase):
    pass


class DeleteBookForm(BookFormBase):
    pass
