from django.shortcuts import render
from django.views.generic import DetailView

from .models import UserBlog


class UserBlogList(DetailView):
    model = UserBlog
    template_name = 'post_list/post_list.html'