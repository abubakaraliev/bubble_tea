from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginUserForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class ProfileUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
