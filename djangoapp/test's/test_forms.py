from django.test import TestCase
from djangoapp.forms import ProductForm




class TestForms(TestCase):

    def test_ProductForm_form_valid_data(self):
        form = ProductForm(data={
            'Product_Name':'Cable Charding',
            'User_Name': 'dani',

        })
        self.assertTrue(form.is_valid)



