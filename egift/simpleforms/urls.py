


from . import views
from django.urls import path

urlpatterns = [
    
    path('create/', views.TaskCreateView.as_view(), name='task_create'),
]
