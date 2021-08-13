from .models import Account
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserModel


class CreateAccountForm(UserCreationForm):
    class Meta:
        model = Account
        fields = (
            'email',
            'username',
        )

    def save(self, commit=True):
        account = super(UserCreationForm, self).save(commit=False)
        account.username = self.cleaned_data['username']
        if commit:
            print('111')
            account.save()
        print('222')
        return account


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = [
            'username',
            'password',
        ]
