from django.urls import path

from forumapp.posts import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('posts/', views.posts, name='posts'),
]