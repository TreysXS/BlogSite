from django.contrib.auth.models import User


def search_user(request):
    """
    Search for users by username.
    """
    user_filter = request.GET.get('user-sort')
    qs = User.objects.filter(
        username__icontains=user_filter
    )
    return qs