"""Defines URL for Password Generators"""
from django.urls import path, include

from . import views

app_name = 'password_generators'

urlpatterns = [
    # Home page for Password Generator
    path('', views.index, name='index'),
    path('password/', views.password, name='password'),
    path('about/', views.about, name='about'),
]