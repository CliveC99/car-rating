from . import views
from django.urls import path
from .views import view

urlpatterns = [
    #path('', views.index, name='home'),
    path('', view.as_view(), name='home'),
]