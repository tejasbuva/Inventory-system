from django.test import TestCase
from django.urls import reverse, resolve
from djangoapp.views import login,my_account,additems
from django.http import HttpRequest
from djangoapp.views import home

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith(''))
        self.assertIn('',html)
        self.assertTrue(html.endswith(''))

class TestUrls(TestCase):

    def test_register_url_resolves(self):
         url = reverse('additems')
         found = resolve(url)
         self.assertEquals(found.func, additems)