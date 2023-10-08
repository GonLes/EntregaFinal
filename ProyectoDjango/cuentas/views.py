from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class SignUpView(CreateView):
    form_class= UserCreationForm
    success_url =reverse_lazy("login")
    template_name="registration/signup.html"



