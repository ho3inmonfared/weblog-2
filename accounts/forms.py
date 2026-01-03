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
        
class SignUpForm(UserCreationForm):
    class Meta:
        model=models.CustomUser
        fields=['username','email','password1','password2']