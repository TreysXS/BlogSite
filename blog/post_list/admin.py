from django.contrib import admin

from .models import Comment, Post, UserBlog, LikePost

admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(UserBlog)
admin.site.register(LikePost)
