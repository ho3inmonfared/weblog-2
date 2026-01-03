from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from . import models,forms

class SignUp(generic.CreateView):
    model=models.CustomUser
    form_class=forms.SignUpForm
    template_name='registration/signup.html'
    success_url=reverse_lazy('login')