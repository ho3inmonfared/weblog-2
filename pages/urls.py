from django.urls import path
from . import views

urlpatterns = [
    path('',views.homeview,name='home'),
    path('detail/<int:pk>',views.PostDetail.as_view(),name='post_detail'),
    path('update/<int:pk>',views.PostUpdate.as_view(),name='post_update'),
    path('delete/<int:pk>',views.PostDelete.as_view(),name='post_delete'),
    path('mypost/',views.MyPosts.as_view(),name='mypost'),
    path('mydrafts/',views.MyDrafts.as_view(),name='mydrafts'),
]
