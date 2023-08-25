from django import forms
from .models import Post, Category, Comments

categories = Category.objects.all().values_list('name', 'name')

categories_list = []

for item in categories:
    categories_list.append(item)


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'content', 'image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'user', 'type':'hidden'}),
            'category': forms.Select(choices=categories_list, attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }


class AddComment(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('name', 'content')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }
