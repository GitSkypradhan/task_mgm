from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.contrib.auth.forms import PasswordResetForm



class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','role','email','username', 'password1', 'password2']
        widget = {
            'first_name':forms.TextInput(attrs={'class': 'form-control'}),
            'role':forms.Select(attrs={'class': 'form-control'}),
            'email':forms.EmailInput(attrs={'class': 'form-control'}),
            'username':forms.TextInput(attrs={'class': 'form-control'}),
            'password1':forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2':forms.PasswordInput(attrs={'class': 'form-control'}),
        }



class CustomPasswordResetForm(PasswordResetForm):
    pass  # No modifications needed for this example, but you can customize the form if desired
