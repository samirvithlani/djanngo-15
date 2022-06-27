


from . import views
from django.urls import path

urlpatterns = [
    
    path('index/',views.index),
    path('index1/',views.index1)
]
