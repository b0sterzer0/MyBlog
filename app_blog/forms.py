from django import forms
from .models import PostModel, CommentModel


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ['title', 'author', 'text', 'add_date']


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ['text']
