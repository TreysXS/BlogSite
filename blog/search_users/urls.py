from django.urls import path

from .views import UserList, UserSearch

urlpatterns = [
    path('list/', UserList.as_view(), name='user-list'),
    path('search/', UserSearch.as_view(), name='user-search')
]