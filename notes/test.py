from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from notes.models import Note


class NoteTests(TestCase):
    def setUp(self):
        # Arrange: Create a user and a note instance to be used in the tests.
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client = Client()
        # Act: Log in the client as the created user.
        self.client.login(username='testuser', password='12345')
        # Continuing with Arrange after Act, since the setup is part of the
        # arrangement for the actual tests.
        self.note = Note.objects.create(
            title='Test Note',
            content='Test content',
            author=self.user
        )

    def test_note_list_view(self):
        # Act: Make a GET request to the 'note_list' view.
        response = self.client.get(reverse('note_list'))
        # Assert: Check if the response is as expected.
        # Assert that the response status code is 200.
        self.assertEqual(response.status_code, 200)
        # Assert that the correct template was used.
        self.assertTemplateUsed(response, 'notes/note_list.html')
        # Assert that the response contains the text 'Test Note'.
        self.assertContains(response, 'Test Note')

    def test_note_detail_view(self):
        # Act: Make a GET request to the 'note_detail' view for the specific
        # note.
        response = self.client.get(reverse('note_detail', args=[self.note.pk]))
        # Assert: Check if the response is as expected.
        # Assert that the response status code is 200.
        self.assertEqual(response.status_code, 200)
        # Assert that the correct template was used.
        self.assertTemplateUsed(response, 'notes/note_detail.html')
        # Assert that the response contains the note's title.
        self.assertContains(response, 'Test Note')
        # Assert that the response contains the note's content.
        self.assertContains(response, 'Test content')

    def test_note_create_view(self):
        # Arrange: Prepare the data for creating a new note.
        # # In this case, the data is being prepared directly in the POST
        # request.
        # # Act: Send a POST request to create a new note.
        response = self.client.post(reverse('note_new'), {
            'title': 'New Note',
            'content': 'New content',
        })
        # Assert: Verify that the response and note creation are as expected.
        # Assert that the response status code is a redirect (302).
        self.assertEqual(response.status_code, 302)
        # Assert that the note was created successfully.
        self.assertTrue(Note.objects.filter(title='New Note').exists())

    def test_note_edit_view(self):
        # Act: Send a POST request to edit the note with new data.
        response = self.client.post(reverse('note_edit', args=[self.note.pk]), {
            'title': 'Updated Note',
            'content': 'Updated content',
        })
        # Assert: Verify that the response and note update are as expected.
        # Assert that the response status code is a redirect (302).
        self.assertEqual(response.status_code, 302)
        # Refresh the note from the database to get the updated values.
        self.note.refresh_from_db()
        # Assert that the note's title has been updated.
        self.assertEqual(self.note.title, 'Updated Note')
        # Assert that the note's content has been updated.
        self.assertEqual(self.note.content, 'Updated content')

    def test_note_delete_view(self):
        # Act: Send a POST request to delete the note.
        response = self.client.post(reverse('note_delete', args=[self.note.pk]))
        # Assert: Verify that the response and note deletion are as expected.
        # Assert that the response status code is a redirect (302).
        self.assertEqual(response.status_code, 302)
        # Assert that the note no longer exists in the database.
        self.assertFalse(Note.objects.filter(pk=self.note.pk).exists())
