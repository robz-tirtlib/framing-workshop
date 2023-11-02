from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=100)
    password = forms.CharField(max_length=64)
    password2 = forms.CharField(max_length=64)
