from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from authentication.models import CustomUser

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username",
                  "email",
                  "first_name",
                  "last_name",
                  "password1",
                  "password2")


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email")
