from django.forms import ModelForm

from .models import Comment


class CommentCreateForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
