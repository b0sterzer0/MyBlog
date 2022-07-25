from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class ProfileForm(forms.Form):
    first_name = forms.CharField(max_length=30, help_text=_('first name'))
    last_name = forms.CharField(max_length=30, help_text=_('last name'))
    email = forms.EmailField(help_text=_('email'))
    city = forms.CharField(max_length=40, help_text=_('city'))
    date_of_birth = forms.DateField(help_text=_('date of birth'))
    hobby = forms.CharField(help_text=_('hobby'))


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, required=True, help_text=_('username'))
    password = forms.CharField(widget=forms.PasswordInput, help_text=_('password'))


class RegisterForm(UserCreationForm):
    email = forms.EmailField(help_text=_('email'))
    city = forms.CharField(max_length=40, help_text=_('city'))
    date_of_birth = forms.DateField(help_text=_('date of birth'))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')
