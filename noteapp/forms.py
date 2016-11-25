from django import forms
from noteapp.models import Note


class NoteForm(forms.ModelForm):
    text = forms.CharField(max_length=500, help_text='Enter note')

    class Meta:
        model = Note
        fields = ('text',)
