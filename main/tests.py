from django.test import TestCase
from django.urls import reverse


# index_view page
class IndexPageTestCase(TestCase):
    # test that index page returns a 200
    def test_index_page(self):
        response = self.client.get(reverse('main:index'))
        self.assertEqual(response.status_code, 200)


# mentions_view page
class MentionsPageTestCase(TestCase):
    # test that page returns a 200
    def test_mentions_page_return_200(self):
        response = self.client.get(reverse('main:mentions'))
        self.assertEqual(response.status_code, 200)
