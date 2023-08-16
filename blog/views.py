from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


#def index(request):
#    return render(request, 'index.html', {})


class view(ListView):
    model = Post
    template_name = 'index.html'


class PostDetail(DetailView):
    model = Post
    template_name = 'post_details.html'
