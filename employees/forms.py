
from django import forms
from .models import *
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm


class CreateEmpForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class CheckInForm(forms.Form):
    empname = forms.CharField(max_length=100)
    place = forms.CharField(max_length=100)
    # You can customize this form based on your requirements

