from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile,Project


class RegisterUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1', 'password2']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture','bio']

class NewProjectForm(forms.ModelForm):
    title = forms.CharField(required=True)
    image = forms.ImageField(required=True)
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'input is-medium'}), required=True)
    url = forms.URLField(required=True)

    class Meta:
        model = Project
        fields = ('title', 'image', 'description', 'url')

