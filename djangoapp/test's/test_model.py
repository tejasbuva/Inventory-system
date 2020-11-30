from django.test import TestCase
from djangoapp.models import Product
from django.contrib.auth.models import User
from mixer.backend.django import mixer


class TestModels(TestCase):

    def setUp(self):
        user = User.objects.create(username='Mahmood', email='a@a.com')
        product = mixer.blend('djangoapp.product', Product_Name=product_Name, Description='100')


def test_content_content(self):
    product1 = Product.objects.get(pk=1)
    first_description = product1.description
    self.assertEquals(first_description, '100')


def test_Product_Name_content(self):
    product = Product.objects.get(id=1)
    first_Product_Name = product.Product_Name
    self.assertEquals(first_Product_Name, 'Product_Name1')


def test_get_absolute_url(self):
    product = Product.objects.get(id=1)
    self.assertEquals(product.get_absolute_url(), '/product/1/')

