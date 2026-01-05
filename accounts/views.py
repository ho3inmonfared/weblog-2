from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from . import models,forms

class SignUp(generic.CreateView):
    model=models.CustomUser
    form_class=forms.SignUpForm
    template_name='registration/signup.html'
    success_url=reverse_lazy('login')
    
class UserProfile(LoginRequiredMixin,generic.DetailView):
    model=models.CustomUser
    template_name = 'accounts/profile.html'
    context_object_name='profile_user'
    
    def get_object(self):
        return self.request.user
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_count'] = self.request.user.post_set.count()
        context['draft_count'] = self.request.user.post_set.filter(status='drf').count()
        return context