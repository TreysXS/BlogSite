from django.shortcuts import redirect
from django.views.generic import DetailView

from .forms import PostForm, CommentForm
from .service import like_or_unlike_post, create_post
from .models import UserBlog


class UserBlogDetail(DetailView):
    """
    Shows the blog page.
    """
    model = UserBlog
    template_name = 'post_list/post_list.html'

    def post(self, request, pk):
        """
        Saves the post and its comments. Likes or dislikes the post.
        """
        post_id = request.POST.get('post_id')
        post_form = PostForm(request.POST)
        comment_form = CommentForm(request.POST)

        if post_form.is_valid():
            create_post(post_form, pk)

        if comment_form.is_valid():
            comment_form.save()

        if post_id is not None:  # check push like
            like_or_unlike_post(request, post_id)

        return redirect('post-list', pk)

