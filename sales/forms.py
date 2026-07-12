from django import forms
from .models import Customer, Sale, SaleItem


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"


class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = "__all__"


class SaleItemForm(forms.ModelForm):
    class Meta:
        model = SaleItem
        fields = "__all__"