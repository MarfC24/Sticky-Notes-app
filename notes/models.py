from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Author(models.Model):
    """
    Represents an author of a note.
    Attributes:
        name (str): The name of the author.
    """
    name = models.CharField(max_length=150)

    def __str__(self):
        """
        Returns the string representation of the Author.
        """
        return self.name


class Note(models.Model):
    """
    Represents a note created by a user.

    Attributes:
        title (models.CharField): The title of the note, up to 150 characters.
        content (models.TextField): The full text content of the note.
        author (models.ForeignKey): A foreign key to the User model,
        representing the note's author. If the author is deleted, the note is
        also deleted (models.CASCADE).
        created_date (models.DateTimeField): The date and time when the note
        was created. Defaults to the current time when the note is created.
        modified_date (models.DateTimeField): The date and time when the note
        was last modified. Automatically updated to the current time each time
        the note is saved.

    Methods:
        __str__(self):
            Returns a string representation of the note, which is the title of
            the note.
    """
    title = models.CharField(max_length=150)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Returns the string representation of the Author.
        """
        return self.title
