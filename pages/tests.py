from django.test import TestCase
from django.urls import reverse

class TestHomePage(TestCase):
    def test_home_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/index.html')

class TestAboutPage(TestCase):
    def test_home_page(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/about_us.html')
