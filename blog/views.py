from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comments, Contact
from .forms import CreatePostForm, AddComment, ContactForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from . import views

# Likes View


def Likes(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse('post-details', args=[str(pk)]))

# Puts the posts on the index.html page
# Puts the newest post first


class view(ListView):
    model = Post
    template_name = 'index.html'
    ordering = ['-created_on']

# Posts the post on the post_details.html page
# Checks if the post is liked and shows the likes count


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

# Shows the form for create_post.html


class CreatePost(CreateView):
    model = Post
    form_class = CreatePostForm
    template_name = 'create_post.html'

# Shows the form for add_comment.html
# Posts the comment to the post
# When complete return to the home page


class AddComment(CreateView):
    model = Comments
    form_class = AddComment
    template_name = 'add_comments.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('home')

# Shows the form for edit_post.html


class EditPost(UpdateView):
    model = Post
    form_class = CreatePostForm
    template_name = 'edit_post.html'

# Shows the delete_post.html page
# When complete return home


class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

# Shows the form for contact.html
# Shows the contact.html page
# When complete direct to form_success.html


class Contact(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = reverse_lazy('form_success')

# When form is successful return to form_success.html


def FormSuccess(request):
    return render(request, 'form_success.html', {})
