from django.test import TestCase
from django.urls import reverse


class WebsitePagesTests(TestCase):
    def test_home_page_loads(self):
        response = self.client.get(reverse('home:index'))
        self.assertEqual(response.status_code, 200)

    def test_contact_page_loads(self):
        response = self.client.get(reverse('contact:contact'))
        self.assertEqual(response.status_code, 200)
