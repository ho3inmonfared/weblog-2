from django.db import models
from accounts.models import CustomUser
class Post(models.Model):
    
    title=models.CharField(max_length=100)
    description=models.TextField()
    author=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    STATUS_CHOICES=(
        ('pub','عمومی'),
        ('drf','پیش نویس'),
    )
    status=models.CharField(choices=STATUS_CHOICES,max_length=100,default='drf')
    
    def __str__(self):
        return self.title
    
