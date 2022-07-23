from django.test import TestCase
from django.contrib.auth.forms import UserCreationForm


class Register(TestCase):

    def test_form_has_fields(self):
        form = UserCreationForm()
        expected = ['username', 'password1', 'password2']
        actual = list(form.fields)
        self.assertSequenceEqual(expected, actual)
