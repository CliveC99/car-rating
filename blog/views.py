from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post


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
    template_name = 'create_post.html'
    fields = '__all__'
    fields = ('title', 'author', 'content')
