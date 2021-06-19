from django.urls import path

from .views import UserBlogList

urlpatterns = [
    path('<int:pk>', UserBlogList.as_view(), name='blog')
]
