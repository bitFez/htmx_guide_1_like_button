from django.urls import path

from .import views 

app_name = 'posts'

urlpatterns = [
    path('post/<int:id>', views.view_post, name='view_post'),
    path('like/<int:id>', views.like_post, name='like_post'),
]
