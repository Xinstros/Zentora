from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import ZentoraUser, Task

#signup form
class SignupForm(UserCreationForm):
    account_type = forms.ChoiceField(choices=ZentoraUser.ACCOUNT_TYPES)
    class Meta:
        model = ZentoraUser
        fields = ['username', 'email', 'password1', 'password2', 'account_type']

 #task form 
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline', 'status']
        widgets = {'deadline': forms.DateInput(attrs={'type': 'date'}),
        }