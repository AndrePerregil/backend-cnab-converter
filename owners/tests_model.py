from django.forms import ValidationError
from django.test import TestCase

from owners.models import User

class UserModelTest(TestCase):
    def test_creation_of_an_user(self):
        username = "someName"
        user = User(username = username)

        self.assertEqual(user.username, username)

    def test_creation_of_invalid_user(self):
        username = "thisIsTooBigForUsernameField"
        user = User(username = username)

        self.assertEqual(user.username, username)