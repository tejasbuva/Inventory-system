from django.urls import reverse, resolve
from django.test import TestCase
from djangoapp.views import home,summary,additems
from djangoapp.models import *


class Test(TestCase):

    def test_root_url_resolves_to_additems_page_view(self):
        path = reverse('additems')
        found = resolve(path)
        self.assertEqual(found.func, additems)

    def test_root_url_resolves_to_home_page_view(self):
        path = reverse('home')
        found = resolve(path)
        self.assertEqual(found.func, home)



    def test_root_url_resolves_to_summary_view(self):
        path = reverse('summary')
        found = resolve(path)
        self.assertEqual(found.func, summary)




