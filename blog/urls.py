from django.urls import path
from .views import *

urlpatterns = [
    path('', PostView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', CreatePostView.as_view(), name='post_new'),
]
