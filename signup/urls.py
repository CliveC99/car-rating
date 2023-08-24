from django.urls import path
from .views import UserSignup, ProfileEdit

urlpatterns = [
    path('register/', UserSignup.as_view(), name='register'),
    path('edit_profile/', ProfileEdit.as_view(), name='edit_profile'),
]
