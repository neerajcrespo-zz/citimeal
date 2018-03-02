from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm, Textarea
from .models import Address

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Your username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Your password"}))

class RegisterForm(forms.Form):
    username  = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Your username"}))
    email     = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"Your email"}))
    password  = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Your password"}))
    password2 = forms.CharField(label="Confirm password",widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Confirm your password"}))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username is taken")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email is taken")
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password2!=password:
            raise forms.ValidationError("Passwords must match")
        return data

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
