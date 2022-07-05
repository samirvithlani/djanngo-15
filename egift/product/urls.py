


from . import views
from django.urls import path
from .views import *

urlpatterns = [
    
    path('index/',views.index),
    path('index1/',views.index1),
    path('demo/',DemoCreateView.as_view()),
]
