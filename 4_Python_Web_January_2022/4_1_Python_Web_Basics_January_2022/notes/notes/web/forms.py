from django import forms

from notes.web.models import Profile, Note


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        labels = {
            'image_url': 'Link to Profile Image',
        }


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = [
            'title',
            'content',
            'image_url',
        ]
        labels = {
            'image_url': 'Link to Image'
        }


class AddNoteForm(NoteForm):
    pass


class EditNoteForm(NoteForm):
    pass


class DeleteNoteForm(NoteForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
