from . import views
from django.urls import path
from .views import view, PostDetail, CreatePost, EditPost, DeletePost, Likes, AddComment, Contact
from signup.views import PasswordsChangeView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', view.as_view(), name='home'),
    path('car/<int:pk>', PostDetail.as_view(), name='post-details'),
    path('create_post/', CreatePost.as_view(), name='create_post'),
    path('car/edit/<int:pk>', EditPost.as_view(), name='edit_post'),
    path('car/<int:pk>/delete', DeletePost.as_view(), name='delete_post'),
    path('like/<int:pk>', Likes, name='likes'),
    path('car/<int:pk>/comment/', AddComment.as_view(), name='add_comment'),
    path('contact/', Contact.as_view(), name='contact'),
    path('<int:uid>/password/', PasswordsChangeView.as_view(template_name='registration/change_password.html'))
]

