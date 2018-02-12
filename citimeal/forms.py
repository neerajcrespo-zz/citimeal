from django import forms
from django.forms import ModelForm, Textarea
from .models import Address

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = [
            'name',
            'phone',
            'address',
        ]
        widgets = {
            'name'    : forms.TextInput(attrs={"class":"form-control","placeholder":"Your full name"}),
            'phone'   : forms.TextInput(attrs={"class":"form-control","placeholder":"Your mobile number"}),
            'address' : forms.TextInput(attrs={"class":"form-control","placeholder":"Your address"}),
        }
