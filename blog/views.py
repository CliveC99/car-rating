from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import CreatePostForm
from django.urls import reverse_lazy

#   def index(request):
#    return render(request, 'index.html', {})


class view(ListView):
    model = Post
    template_name = 'index.html'
    ordering = ['-created_on']


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

class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
