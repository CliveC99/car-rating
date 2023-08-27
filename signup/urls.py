from django.urls import path
from .views import UserSignup, ProfileEdit

# Urls to redirct to the register.html and edit_profile.html page
urlpatterns = [
    path('register/', UserSignup.as_view(), name='register'),
    path('edit_profile/', ProfileEdit.as_view(), name='edit_profile'),
]
