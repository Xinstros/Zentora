from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import ZentoraUser

class SignupForm(UserCreationForm):
    account_type = forms.ChoiceField(choices=ZentoraUser.ACCOUNT_TYPES)

    class Meta:
        model = ZentoraUser
        fields = ['username', 'email', 'password1', 'password2', 'account_type']