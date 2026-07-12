from django import forms
from .models import Finance


class FinanceForm(forms.ModelForm):
    class Meta:
        model = Finance
        fields = "__all__"

        widgets = {
            "transaction_date": forms.DateInput(
                attrs={"type": "date"}
            ),
        }