import datetime

from django import forms


class ProductForm(forms.Form):
    name = forms.CharField(label='Product name', max_length=100)
    price = forms.DecimalField(label='Product price', max_digits=10, decimal_places=2)
    description = forms.CharField(label='Product description', widget=forms.Textarea)
    amount = forms.IntegerField(label='Product amount')
    add_date = forms.DateField(initial=datetime.date.today,
                               widget=forms.DateInput(attrs={'type': 'date'}))
    image = forms.ImageField(label='Product image', required=False)
