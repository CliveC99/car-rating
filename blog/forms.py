from django import forms
from .models import Post, Category, Comments, Contact

categories = Category.objects.all().values_list('name', 'name')

categories_list = []

for item in categories:
    categories_list.append(item)

# Form for create_post.html


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'content', 'image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'id':'user', 'type': 'hidden'}),
            'category': forms.Select(choices=categories_list, attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }

# Form for add_comment.html


class AddComment(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('name', 'content')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }

# Form for contact.html


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('username', 'email', 'content')

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'id': 'user'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }