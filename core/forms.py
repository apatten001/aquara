from django import forms
from .models import User
from django_countries.widgets import CountrySelectWidget


class RegisterForm(forms.ModelForm):
    password = forms.PasswordInput()

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password', 'username', 'country']
        widgets = {'country': CountrySelectWidget()}


class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['email', 'password']


