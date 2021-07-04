from django.views.generic import ListView

from django.contrib.auth.models import User
from .service import search_user


class UserList(ListView):
    """
    Shows all list user's.
    """
    model = User
    template_name = 'search_users/user_list.html'


class UserSearch(ListView):
    """
    Shows users filtered by username.
    """
    template_name = 'search_users/user_search.html'

    def get_queryset(self):
        qs = search_user(self.request)
        return qs


