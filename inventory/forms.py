from django import forms
from .models import (
    Category,
    Supplier,
    Product,
    StockTransaction,
    PurchaseOrder,
    PurchaseOrderItem,
)


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = "__all__"


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


class StockTransactionForm(forms.ModelForm):
    class Meta:
        model = StockTransaction
        fields = "__all__"


class PurchaseOrderForm(forms.ModelForm):
    class Meta:
        model = PurchaseOrder
        fields = "__all__"


class PurchaseOrderItemForm(forms.ModelForm):
    class Meta:
        model = PurchaseOrderItem
        fields = "__all__"