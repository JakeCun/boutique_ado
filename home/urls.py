
from django.contrib import admin
from django.urls import path, include
from .templates.home import views

urlpatterns = [
    path('', views.index, name='home')
]
