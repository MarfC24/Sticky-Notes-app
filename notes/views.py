from django.shortcuts import render, get_object_or_404, redirect
from .form import NoteForm, RegisterForm
from django.contrib.auth.decorators import login_required
from .models import Note
from django.contrib.auth import authenticate, logout as auth_logout


def logout_view(request):
    """
    Log out the user and redirect to the login page.
    """
    auth_logout(request)
    return redirect('login')


@login_required
def note_list(request):
    """
    This View function lists all notes created by the currently logged-in user.

    This view is protected with the @login_required decorator, ensuring that
    only authenticated users can access this view.

    Args:
        request: HttpRequest object containing metadata about the request.

    Returns:
        HttpResponse object that renders 'notes/note_list.html' with a
        context dictionary
        containing a 'notes' key that holds the queryset of Note objects
        authored by the request.user.
    """
    notes = Note.objects.filter(author=request.user)
    return render(request, 'notes/note_list.html', {'notes': notes})


@login_required
def note_detail(request, pk):
    """
    This View function displays the detail of a single note.

    This view is protected with the @login_required decorator to ensure that
    only authenticated users can access the details of a note. It retrieves a
    note by its primary key (pk) or raises a 404 error if the note does not
    exist.

    Args:
        request: HttpRequest object containing metadata about the request.
        pk: The primary key of the Note object to retrieve.

    Returns:
        HttpResponse object that renders 'notes/note_detail.html' with a
        context dictionary
        containing a 'note' key that holds the Note object retrieved based on
        the provided pk.
    """
    note = get_object_or_404(Note, pk=pk)
    return render(request, 'notes/note_detail.html', {'note': note})


@login_required
def note_new(request):
    """
    View function for creating a new note.

    This view is protected with the @login_required decorator, ensuring that
    only authenticated users can create a new note. If the request method is
    POST, it processes the form data to create a new Note object. If the form
    is valid, it saves the new note with the current user as the author and
    redirects to the note's detail page. If the request method is not POST,
    it displays an empty form for creating a new note.

    Args:
        request: HttpRequest object containing metadata about the request.

    Returns:
        If POST and form is valid, redirects to 'note_detail' view for the
        new note.
        Otherwise, renders 'notes/note_edit.html' with a context dictionary
        containing a 'form' key with a NoteForm instance.
    """
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user
            note.save()
            return redirect('note_detail', pk=note.pk)
    else:
        form = NoteForm()
    return render(request, 'notes/note_edit.html', {'form': form})


@login_required
def note_edit(request, pk=None):
    """
    View function for editing an existing note or creating a new one.

    This view is protected with the @login_required decorator to ensure that
    only authenticated users can edit or create a note. If a primary key (pk)
    is provided, the function attempts to retrieve an existing note; otherwise,
    it initializes a new Note object. If the request method is POST, the
    submitted form data is processed. If the form is valid, the note is saved
    and the user is redirected to the note's detail page. If the request method
    is not POST, the form is pre-populated with the note's data for editing.

    Args:
        request: HttpRequest object containing metadata about the request.
        pk: Optional; The primary key of the Note object to edit. Defaults to
        None.

    Returns:
        If POST and form is valid, redirects to 'note_detail' view for the
        edited or new note.
        Otherwise, renders 'notes/note_edit.html' with a context dictionary
        containing a 'form' key with a NoteForm instance and a 'note' key with
        the Note object.
    """
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user
            note.save()
            return redirect('note_detail', pk=note.pk)
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/note_edit.html', {'form': form, 'note': note})


@login_required
def note_delete(request, pk):
    """
    View function for deleting a specific note.

    This view is protected with the @login_required decorator, ensuring that
    only authenticated users can delete a note. It retrieves the note by its
    primary key (pk) or raises a 404 error if the note does not exist. If the
    request method is POST, the note is deleted and the user is redirected to
    the list of their notes. If the request method is not POST, a confirmation
    page for deletion is rendered.

    Args:
        request: HttpRequest object containing metadata about the request.
        pk: The primary key of the Note object to be deleted.

    Returns:
        If the request method is POST, redirects to 'note_list' view.
        Otherwise, renders 'notes/note_delete.html' with a context dictionary
        containing a 'note' key with the Note object to be deleted.
    """
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        note.delete()
        return redirect('note_list')
    return render(request, 'notes/note_delete.html', {'note': note})
