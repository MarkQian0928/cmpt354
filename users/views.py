from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm, CustomUserChangeForm

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class UpdateInfo(generic.CreateView):
    form_class = CustomUserChangeForm
    template_name = 'updateInfo.html'