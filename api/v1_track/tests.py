import io
from unittest import mock

from django.core.files import File
from django.test import TestCase
from rest_framework.test import APITestCase

from .models import Track


class TrackAPIViewTest(APITestCase):

    def test_get_request_tracks(self):
        response = self.client.get('/api/v1/tracks/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_permission(self):
        response = self.client.get('/api/v1/tracks/', follow=True)
        not_expected = {
            'detail': 'Authentication credentials were not provided.',
        }
        self.assertNotEqual(response.json(), not_expected)


class TrackModelTest(TestCase):

    @mock.patch('django.core.files.storage.FileSystemStorage.save')
    def test_can_create_track(self, mock_save):
        mock_save.return_value = 'track_one.mp3'
        file = File(io.BytesIO(b'track_one'), name='track_one.mp3')
        track_one = Track.objects.create(name='track_one', file=file)
        self.assertEqual(Track.objects.first().name, track_one.name)
        self.assertEqual(Track.objects.first().file.name, file.name)
        mock_save.assert_called_once()  # No files saved


class TrackSerializerTest(APITestCase):

    @mock.patch('django.core.files.storage.FileSystemStorage.save')
    def test_if_we_can_post_audio_file(self, mock_save):
        mock_save.return_value = 'test_file.mp3'
        file = io.BytesIO(b'this is a music')
        file.name = 'test_file.mp3'
        payload = {
            'file': file,
            'name': 'test_file.mp3',
        }
        response = self.client.post(
            '/api/v1/tracks/', data=payload, follow=True,
        )
        self.assertEqual(response.status_code, 201)
        mock_save.assert_called_once()

    def test_if_passing_not_audio_file(self):
        file = io.BytesIO(b'this is not a music')
        file.name = 'test_file.docx'
        payload = {
            'file': file,
            'name': 'test_file.docx',
        }
        response = self.client.post(
            '/api/v1/tracks/', data=payload, follow=True,
        )
        self.assertIn(
            'This field must be supplied with an audio file',
            response.content.decode(),
        )
        self.assertEqual(response.status_code, 400)
