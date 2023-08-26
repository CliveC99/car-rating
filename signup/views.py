from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import RegistrationForm, EditProfile, PasswordUpdatingForm


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordUpdatingForm
    success_url = reverse_lazy('home')


class UserSignup(generic.CreateView):
    form_class = RegistrationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class ProfileEdit(generic.UpdateView):
    form_class = EditProfile
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
