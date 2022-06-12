from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class RegisterUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first name','last name','email','username','password1', 'password2']