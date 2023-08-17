from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from .forms import CreatePostForm

#   def index(request):
#    return render(request, 'index.html', {})


class view(ListView):
    model = Post
    template_name = 'index.html'


class PostDetail(DetailView):
    model = Post
    template_name = 'post_details.html'


class CreatePost(CreateView):
    model = Post
    form_class = CreatePostForm
    template_name = 'create_post.html'


class EditPost(UpdateView):
    model = Post
    form_class = CreatePostForm
    template_name = 'edit_post.html'
    
