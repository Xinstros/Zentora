from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import ZentoraUser, Task, Request, Artwork

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
#Art request for for Devs
class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['title', 'description', 'style', 'genre', 'deadline', 'reward_type', 'reward_amount']
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'}),
        }
#Artwork submit form
class ArtworkForm(forms.ModelForm):
    class Meta:
        model = Artwork
        fields = ['title', 'file', 'license', 'price']