from django.shortcuts import render
from django.views.generic.edit import CreateView

from .models import Task
from .forms import TaskForm

# Create your views here.
class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "sf/task_form.html"
    success_url = "/"