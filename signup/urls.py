from django.urls import path
from .views import UserSignup


urlpatterns = [
    path('register/', UserSignup.as_view(), name='register'),
]