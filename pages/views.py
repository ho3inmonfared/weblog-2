from django.shortcuts import render
from django.views import generic
from posts import models

# class Home(generic.TemplateView):
#     template_name='pages/home.html'

def homeview(request):
    posts=models.Post.objects.filter(status='pub').order_by('-created_at')
    
    context={
        'posts':posts
    }
    return render(request,'pages/home.html',context)
    
