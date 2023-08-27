from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import RegistrationForm, EditProfile, PasswordUpdatingForm

# Sets the form to PasswordUpdatingForm
# When complete returns to the home page


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordUpdatingForm
    success_url = reverse_lazy('home')

# Sets the from as RegistrationForm
# Uses the register.html template
# When complete returns to the home page


class UserSignup(generic.CreateView):
    form_class = RegistrationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

# Uses the EditProfile form
# Uses the edit_profile.html template
# When complete returns to the home page
# Auto fills the username field


class ProfileEdit(generic.UpdateView):
    form_class = EditProfile
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
