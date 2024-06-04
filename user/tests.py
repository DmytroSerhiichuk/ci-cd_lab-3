from django.test import TestCase
from django.urls import reverse
from user.models import User

# Create your tests here.

class AuthTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(email='test@test.com', password='111')

    def test_auth_requirements(self):
        self.client.logout()
        response = self.client.get(reverse('user:profile'))
        self.assertEqual(response.status_code, 302)

        self.client.login(email='test@test.com', password='111')
        response = self.client.get(reverse('user:profile'))
        self.assertEqual(response.status_code, 200)
