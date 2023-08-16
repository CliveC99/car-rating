from . import views
from django.urls import path
from .views import view, PostDetail

urlpatterns = [
#    path('', views.index, name='home'),
    path('', view.as_view(), name='home'),
    path('car/<int:pk>', PostDetail.as_view(), name='post-details'),
]