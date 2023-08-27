from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField


STATUS = ((0, "Draft"), (1, "Published"))

# Model for Category
# Shows name in admin panel
# When complete return home


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

# Model for posts
# Shows post name in admin panel
# return home after post is made


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    image = models.ImageField(null=True, upload_to="media/")
    title_tag = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True, null=True)
    category = models.TextField(default='VAG')
    likes = models.ManyToManyField(User, related_name='carreview')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')

# Model for comments
# Shows title and author in admin panel


class Comments(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s ---- %s' % (self.post.title, self.name)

# Model for Contact
# Shows username and email in admin panel


class Contact(models.Model):
    content = models.TextField(max_length=500)
    email = models.EmailField()
    username = models.CharField(max_length=250)

    def __str__(self):
        return '%s ---- %s' %  (self.username, self.email)