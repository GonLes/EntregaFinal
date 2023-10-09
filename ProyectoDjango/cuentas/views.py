from typing import Any
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from django.shortcuts import render , get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView , UpdateView , DetailView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SignUpForm , EditProfileForm
from blog.models import Avatar




# Create your views here.
class EditProfileView(UpdateView):
    model=Avatar
    template_name='registration/edit_profile_page.html'
    fields=['imagen','url_linkedin','url_github','bio']
    success_url =reverse_lazy("home")

class ShowProfileView(DetailView):
    model= Avatar
    template_name="registration/user_profile.html"

    def get_context_data(self,*args, **kwargs):
        #users=Avatar.objects.all()
        context=super(ShowProfileView,self).get_context_data(*args,**kwargs) 
        page_user=get_object_or_404(Avatar,id=self.kwargs['pk']) 
        context["page_user"]=page_user
        return context


class SignUpView(CreateView):
    form_class= SignUpForm
    success_url =reverse_lazy("login")
    template_name="registration/signup.html"

class UserEditView(UpdateView):
    form_class= EditProfileForm
    success_url =reverse_lazy("home")
    template_name="registration/edit_profile.html"
    
    def get_object(self):
        return self.request.user
        




