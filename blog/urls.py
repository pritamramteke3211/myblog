
from django.urls import path
from . import views


urlpatterns = [
    path('',views.BlogHomePage.as_view(),name='bhome'),
    path('blogpost/<int:id>',views.blogpost,name='blogpost'),
    path('blogsearch/',views.blogsearch,name='blogsearch'),
    path('blogcomment/<int:post_id>',views.blogComment,name='blogcomment'),
    path('blog_dashboard',views.blog_dashboard,name='blog_dashboard'),
    
]