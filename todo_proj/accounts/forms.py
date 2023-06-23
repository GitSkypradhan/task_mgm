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

class CustomPasswordResetForm(PasswordResetForm):
    pass  # No modifications needed for this example, but you can customize the form if desired
