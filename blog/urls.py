from . import views
from django.urls import path
from .views import view, PostDetail, CreatePost, EditPost

urlpatterns = [
#   path('', views.index, name='home'),
    path('', view.as_view(), name='home'),
    path('car/<int:pk>', PostDetail.as_view(), name='post-details'),
    path('create_post/', CreatePost.as_view(), name='create_post'),
    path('car/edit/<int:pk>', EditPost.as_view(), name='edit_post'),
]