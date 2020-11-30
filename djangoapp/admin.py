from django.contrib import admin

from .forms import ProductForm
from .models import Product


# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ['Product_Name', 'Status', 'Serial_No', 'Issues', 'Cost_in_Euro', 'User_Name', 'Product_Group',
                    'Description', 'Purchase_Date', 'Date_Modified']
    form = ProductForm
    list_filter = ['Product_Name', 'Status', 'Serial_No', 'Issues', 'Cost_in_Euro', 'User_Name', 'Product_Group',
                   'Description']
    search_fields = ['Product_Name', 'Status', 'Serial_No', 'Issues', 'Cost_in_Euro', 'User_Name', 'Product_Group',
                     'Description']


admin.site.register(Product, ProductAdmin)
