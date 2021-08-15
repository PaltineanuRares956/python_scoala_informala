# import django.contrib.auth.admin

from .models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            'email',
            'username',
            'password1',
            'password2',
        )

    def save(self, commit=True):
        account = super(UserCreationForm, self).save()
        account.password = self.cleaned_data['password1']
        account.save()
        return account


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]
