from django.urls import path
from . import views

urlpatterns = [
    path('',views.homeview,name='home'),
    path('detail/<int:pk>',views.PostDetail.as_view(),name='post_detail'),
]
