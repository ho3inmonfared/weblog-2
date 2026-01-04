from django.shortcuts import render,redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from posts import models,forms

# class Home(generic.TemplateView):
#     template_name='pages/home.html'

def homeview(request):
    posts=models.Post.objects.filter(status='pub').order_by('-created_at')
    
    if request.method == "POST":
        form=forms.PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect('home')
    else:
        form=forms.PostForm()
    
    context={
        'posts':posts,
        'form':form,
    }
    return render(request,'pages/home.html',context)

class PostDetail(generic.DetailView):
    model=models.Post
    template_name='pages/detail.html'
    context_object_name='post'
    

class PostUpdate(LoginRequiredMixin,generic.UpdateView):
    model=models.Post
    form_class=forms.PostForm
    template_name='pages/update.html'
    
    def get_queryset(self):
        return models.Post.objects.filter(author=self.request.user)
    
    
