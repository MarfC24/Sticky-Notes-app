from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    """
    A ModelForm subclass for creating and editing Note instances.

    This form is linked to the Note model and includes fields for 'title' and
    'content', allowing users to input data for these fields when creating or
    editing a Note.

    Attributes:
        Meta: An inner class that provides metadata to the ModelForm class. It
        defines the model associated with the form and the fields to be
        included in the form.
    """
    class Meta:
        model = Note
        fields = ['title', 'content']
