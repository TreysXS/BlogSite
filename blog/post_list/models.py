from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

import uuid


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    message = models.TextField(max_length=1000, verbose_name='Описание')
    date = models.DateField(auto_now_add=True, editable=False)
    likings = models.ManyToManyField(User)


class Comment(models.Model):
    user = models.ForeignKey('auth.User',  on_delete=models.SET_NULL, null=True)
    message = models.TextField(max_length=1000, verbose_name='Сообщение')
    date = models.DateField(auto_now_add=True, editable=False)
    post = models.ForeignKey('Post', on_delete=models.SET_NULL, blank=True, null=True, related_name='comments')


class UserBlog(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    posts = models.ManyToManyField(Post)

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