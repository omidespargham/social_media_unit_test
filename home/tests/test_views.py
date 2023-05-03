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

    def test_user_register_POST_invalid(self):
        response = self.client.post(reverse("account:user_register"),data={"username":"ali","email":"invalid_email","password1":"omid1234","password2":"omid1111"})
        # self.assertRedirects(response,reverse("account:user_register")) # neveshtane in code inja eshtaba ast zira
        # user redirect nemishavad be account:user_register.va in k assertRedirects khodesh check mikone ke aya status code response
        # 302(redirect) hst ya na.
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'account/register.html')
        self.failIf(response.context["form"].is_valid())
        self.assertFormError(form=response.context['form'],field='email',)
        
    
# class TestWriterViews(TestCase):
#     def setUp(self):
#         User.objects.create_user(username="root",email="root@gmail.com",password="root1234")
#         self.client = Client()
#         self.client.login(username='root',email='root@gmail.com',password='root1234')
    
