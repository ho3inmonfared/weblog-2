from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=models.CustomUser
        fields=UserCreationForm.Meta.fields + ('email',)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model=models.CustomUser
        fields=UserChangeForm.Meta.fields