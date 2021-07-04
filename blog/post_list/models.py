from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

import uuid


class Post(models.Model):
    """
    Post model.
    """
    user = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, related_name='users')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    message = models.TextField(max_length=1000, verbose_name='Описание')
    date = models.DateField(auto_now_add=True, editable=False)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return str(self.id)


class LikePost(models.Model):
    """
    Model of the user who liked the post.
    """
    user = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, related_name='user_like')
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True, related_name='likings')

    def __str__(self):
        return str(self.user)


class Comment(models.Model):
    """
    Model of the comment under the post.
    """
    user_comment = models.ForeignKey('auth.User',  on_delete=models.SET_NULL, null=True)
    message_comment = models.TextField(max_length=1000, verbose_name='Сообщение')
    date = models.DateField(auto_now_add=True, editable=False)
    post = models.ForeignKey('Post', on_delete=models.SET_NULL, blank=True, null=True, related_name='comments')

    def __str__(self):
        return str(self.id)


class UserBlog(models.Model):
    """
    The blog model for the user.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    posts = models.ManyToManyField(Post)

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('post-list', args=[str(self.id)])

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        """
        When a user is created, a profile is also created for him.
        """
        if created:
            UserBlog.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        """
        Updates profile settings for a specific user.
        """
        instance.userblog.save()