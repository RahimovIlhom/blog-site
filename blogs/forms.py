from django.forms import ModelForm

from .models import Comment, Blog


class CommentCreateForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body']


class BlogCreateForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body', 'photo', 'video', 'category', 'tags']
