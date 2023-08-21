from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import CreatePostForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect


def Likes(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse('post-details', args=[str(pk)]))


class view(ListView):
    model = Post
    template_name = 'index.html'
    ordering = ['-created_on']


class PostDetail(DetailView):
    model = Post
    template_name = 'post_details.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PostDetail, self).get_context_data(*args, **kwargs)
        likesnumber = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = likesnumber.total_likes()

        liked = False
        if likesnumber.likes.filter(id=self.request.user.id).exists():
            liked = True
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context


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
