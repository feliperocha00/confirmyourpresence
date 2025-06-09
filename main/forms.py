from django import forms
from .models import Gift

class GiftForm(forms.ModelForm):
    class Meta:
        model = Gift
        fields = ["name", "price", "image_url", "product_url"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
            "image_url": forms.URLInput(attrs={"class": "form-control"}),
            "product_url": forms.URLInput(attrs={"class": "form-control"}),
        }
