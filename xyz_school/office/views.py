from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.http import HttpResponse

#FOR FUNCTION BASED VIEW
from django.contrib.auth.decorators import login_required

#FOR LOGOUT
from django.contrib.auth import logout

#FOR CLASS BASED VIEW
from django.contrib.auth.mixins import LoginRequiredMixin

# FOR SIGNUP
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, DeleteView, UpdateView


# Create your views here.

class SignUp(CreateView):
  form_class = UserCreationForm
  success_url = reverse_lazy("login")
  template_name = "registration/signup.html"


@login_required
def home(request):
  context = {"name": request.user}
  return render(request, 'office/home.html', context)

def logout_view(request):
    logout(request)
    return redirect("home")

# def login_view(request):
#   context = {
#     "login_view": "active"
#   }
#   if request.method == "POST":
#     username = request.POST["username"]
#     password = request.POST["password"]
#     # Add your code below:
#     user=authenticate(request, username=username, password=password)
    
#     if user is not None:
#       return redirect("home")
#     else:
#       return HttpResponse("invalid credentials")
#   return render(request, "registration/login.html", context)

