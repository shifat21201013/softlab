from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "name",
            "blood_group",
            "gender",
            "phone_number",
            "age",
            "national_number",
        ]


class ProductSearchForm(forms.Form):
    search_query = forms.CharField(label='Search', max_length=100)
