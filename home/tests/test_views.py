from django.test import TestCase,Client
from django.urls import reverse
from django.contrib.auth.models import User
from account.forms import UserRegistrationForm
class TestUserRegisterView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_user_register_GET(self):
        response = self.client.get(reverse("account:user_register"))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'account/register.html')
        self.failUnless(response.context['form'],UserRegistrationForm)

    def test_user_register_POST_valid(self):
        response = self.client.post(reverse("account:user_register"),data={"username":"omid",'email':"omid@gmail.com","password1":"omid1234","password2":"omid1234"})
        self.assertEqual(response.status_code,302)
        self.assertRedirects(response,reverse("home:home"))
        self.assertEqual(User.objects.count(),1)
    
