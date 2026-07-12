from django import forms
from .models import (
    PurchaseRequisition,
    PurchaseRequisitionItem,
    SupplierQuotation,
    GoodsReceivedNote,
)


class PurchaseRequisitionForm(forms.ModelForm):
    class Meta:
        model = PurchaseRequisition
        fields = "__all__"


class PurchaseRequisitionItemForm(forms.ModelForm):
    class Meta:
        model = PurchaseRequisitionItem
        fields = "__all__"


class SupplierQuotationForm(forms.ModelForm):
    class Meta:
        model = SupplierQuotation
        fields = "__all__"


class GoodsReceivedNoteForm(forms.ModelForm):
    class Meta:
        model = GoodsReceivedNote
        fields = "__all__"