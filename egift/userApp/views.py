from django.shortcuts import render
from django.views.generic import FormView

from .forms import UserForm

# Create your views here.
class BaseRegisterView(FormView):

    form_class = UserForm
    template_name ="userApp/register.html"
    success_url = "/"
    
    def form_valid(self, form):
        user = form.save()
        user.set_password = form.cleaned_data['password']
        user.save()
        return super().form_valid(form)