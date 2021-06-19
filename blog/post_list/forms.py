from django.forms import ModelForm

from .models import Comment, Post


class PostForm(ModelForm):
    pass

    class Meta:
        model = Post
        exclude = ('id', 'likings')


class CommentForm(ModelForm):
    pass

    class Meta:
        model = Comment
        fields = ('user_comment', 'message_comment', 'post',)