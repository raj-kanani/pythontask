from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('session/', views.setsession, name='session'),
    path('register/', views.user_register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
