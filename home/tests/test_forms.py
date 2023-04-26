from django.test import TestCase
from account.forms import UserRegistrationForm
from django.contrib.auth.models import User

class TestRegistrationForm(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(username="kevin",email="kevin@gmail.com",password="kevin")

    def test_valid_data(self):
        form = UserRegistrationForm(
            data={"username": "jack", "email": "jack@gmail.com", "password1": "jack1234", "password2": "jack1234"})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["username"],"jack")

    def test_empty_data(self):
        form = UserRegistrationForm(data={})
        self.assertFalse(form.is_valid())

    def test_exist_email(self):
        form = UserRegistrationForm(data={"username": "kevin", "email": "kevin@gmail.com", "password1": "jack1234", "password2": "jack1234"})
        self.assertEqual(len(form.errors),1)

    

