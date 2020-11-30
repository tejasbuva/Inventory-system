from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['Product_Name', 'Status', 'Serial_No', 'Issues', 'Cost_in_Euro',
                  # 'User_Name', 'Product_Group',
                  # 'Units', 'Purchase_Date',
                  'Description', 'Tags']

    def clean_Product_Name(self):
        Product_Name = self.cleaned_data.get('Product_Name')
        if Product_Name == '':
            raise forms.ValidationError('This Field Cannot be left blank')
        return Product_Name

    def clean_Serial_No(self):
        Serial_No = self.cleaned_data.get('Serial_No')
        if Serial_No == '':
            raise forms.ValidationError('This Field Cannot be left blank')
        return Serial_No

    def clean_Cost_in_Euro(self):
        Cost_in_Euro = self.cleaned_data.get('Cost_in_Euro')
        if Cost_in_Euro == '':
            raise forms.ValidationError('This Field Cannot be left blank')
        return Cost_in_Euro

    def clean_User_Name(self):
        User_Name = self.cleaned_data.get('User_Name')
        if User_Name == '':
            raise forms.ValidationError('This Field Cannot be left blank')
        return User_Name

    def clean_Product_Group(self):
        Product_Group = self.cleaned_data.get('Product_Group')
        if Product_Group == '':
            raise forms.ValidationError('This Field Cannot be left blank')
        return Product_Group

    def clean_Units(self):
        Unit = self.cleaned_data.get('Unit')
        if Unit == '':
            raise forms.ValidationError('This Field Cannot be left blank')
        return Unit


class ProductSearchForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['Product_Name', 'Serial_No', 'Purchase_Date']
