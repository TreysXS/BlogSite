from .models import UserBlog, Post, LikePost


def create_post(post_form, pk):
    """
    Creates a post for the user's blog.
    """
    post = post_form.save()

    user_blog = UserBlog.objects.get(id=pk)
    user_blog.posts.add(post)


def like_or_unlike_post(request, post_id):
    """
    Implements like or dislike under the post.
    """
    post = Post.objects.get(id=post_id)
    user_like = LikePost.objects.filter(user=request.user, post=post)

    if len(user_like) == 0:
        LikePost.objects.create(user=request.user, post=post)
    else:
        post.likings.get(user=request.user, post=post).delete()