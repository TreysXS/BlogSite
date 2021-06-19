from django.urls import path

from .views import UserBlogDetail

urlpatterns = [
    path('<int:pk>', UserBlogDetail.as_view(), name='post-list')
]
