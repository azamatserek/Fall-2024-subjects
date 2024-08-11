from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_post_list, name='blog_post_list'),
    path('post/<int:post_id>/', views.blog_post_detail, name='blog_post_detail'),
    path('create/', views.create_blog_post, name='create_blog_post'),  # New URL for creating a blog post
]
