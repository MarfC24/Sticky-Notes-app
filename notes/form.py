from django import forms
from .models import Note
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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


class RegisterForm(UserCreationForm):
    """
    Form for registering a new user account.
    Inherits from Django's built-in UserCreationForm and adds an email field.
    """
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        """
        Save the provided password in hashed format and save the email field.
        """
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
