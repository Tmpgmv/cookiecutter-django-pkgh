from django.test import TestCase
from django.urls import reverse

{ % if cookiecutter.custom_user == "y" %}
from accounts.models import User
{ % else %}
from django.contrib.auth.models import User
{ % endif %}

class HomePageTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_home_page_contains_project_name(self):
        """
        На страницу home присутствует ли название проекта?
        """
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('home'))
        html = response.content.decode("utf8")
        self.assertIn("{{ cookiecutter.project_name_rus }}", html)
