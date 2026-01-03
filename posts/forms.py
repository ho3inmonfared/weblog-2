from django import forms
from . import models


class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title', 'description', 'status']

        labels = {
            'title': 'عنوان پست',
            'description': 'توضیحات',
            'status': 'وضعیت انتشار',
        }

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full px-3 md:px-4 py-2 md:py-3 rounded-xl input-field text-sm md:text-base',
                'placeholder': 'عنوان جذاب برای پست خود بنویسید...',
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full px-3 md:px-4 py-2 md:py-3 rounded-xl input-field resize-none text-sm md:text-base',
                'rows': 4,
                'placeholder': 'محتوای پست خود را اینجا بنویسید...',
            }),
            'status': forms.Select(attrs={
                'class': 'w-full px-3 md:px-4 py-2 md:py-3 rounded-xl input-field text-sm md:text-base',
            }),
        }
