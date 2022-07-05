from django.shortcuts import render
from django.views.generic import FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.hashers import make_password

from .forms import UserForm

# Create your views here.
class BaseRegisterView(FormView):

    form_class = UserForm
    template_name ="userApp/register.html"
    success_url = "/"
    
    def form_valid(self, form):
        user = form.save()
        user.is_staff = True
        user.password = make_password(form.cleaned_data['password'])
        print(user.password)
        
        user.save()
        return super().form_valid(form)

class UserLoginView(LoginView):
    template_name = "userApp/login.html"
    success_url ="/"

def profile(request):
    return render(request, "userApp/profile.html")        