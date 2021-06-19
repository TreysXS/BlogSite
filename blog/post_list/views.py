from django.shortcuts import render, redirect
from django.views.generic import DetailView

from .models import UserBlog
from .forms import PostForm, CommentForm


class UserBlogDetail(DetailView):
    model = UserBlog
    template_name = 'post_list/post_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['form'] = CommentForm(self.request.POST)
        return context

    def post(self, request, pk):
        post_form = PostForm(request.POST)
        comment_form = CommentForm(request.POST)

        if post_form.is_valid():
            post = post_form.save()

            user_blog = UserBlog.objects.get(user=request.user)
            user_blog.posts.add(post)

        if comment_form.is_valid():
            comment = comment_form.save()

        return redirect('post-list', pk)

