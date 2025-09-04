from django import forms
from .models import Gift, Guests

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
        
class GuestForm(forms.ModelForm):
    class Meta:
        model = Guests
        fields = ["name", "phone", "parent", "confirm"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control", "step": "0.01"}),
            "parent": forms.Select(attrs={"class": "form-control"}),
            "confirm": forms.CheckboxInput(attrs={"class": "form-control"}),
        }
