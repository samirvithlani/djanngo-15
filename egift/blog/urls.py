from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    
    path('aboutus/',views.aboutUs),
    path('aboutyou/',views.aboutYou),
]
