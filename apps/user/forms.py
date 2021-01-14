from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    profile_photo = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ('username', 'profile_photo', 'password1', 'password2','email')
