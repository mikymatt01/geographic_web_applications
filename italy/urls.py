from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('borders/', views.borders),
    path('geocoding/', views.geocoding),
]