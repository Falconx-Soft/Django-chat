from django.contrib import admin
from django.urls import path

from . import views

from django.contrib.auth import views as auth_views

app_name = 'chat'

urlpatterns = [
    path('', views.home, name="home"),
    path('private_chat/', views.private_chat, name="private_chat"),
    path('create_or_return_private_chat/', views.create_or_return_private_chat, name='create-or-return-private-chat'), # TODO: ADD THIS LINE.
]