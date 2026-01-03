from django.contrib import admin
from django.utils.text import Truncator
from . import models

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display=('title','short_description','author','created_at','status')
    list_filter=('created_at','status',)
    ordering=('-created_at',)
    search_fields=('title',)
    
    def short_description(self,obj):
        return Truncator(obj.description).words(5)
