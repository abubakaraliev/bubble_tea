from django import forms
from .models import newUser, loginForm, accountUpdate ,userInformations



class CreateUserForm(forms.ModelForm):
    class Meta:
        model = newUser
        fields = ['username', 'email', 'password']

class LoginUserForm(forms.ModelForm):
    class Meta:
        model = loginForm
        fields = ['username', 'password']

class AccountUserForm(forms.ModelForm):
    class Meta:
        model = accountUpdate
        fields = ['username', 'email', 'password']

class ProfileUserForm(forms.ModelForm):
    class Meta:
        model = userInformations
        fields = ['firstname', 'lastname', 'phone', 'address', 'postcode', 'city']
