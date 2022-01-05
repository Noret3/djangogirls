from django.shortcuts import render
from django.views.generic import ListView

from .models import Post
from django.utils import timezone


class PostView(ListView):
    model = Post
    queryset = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    context_object_name = 'posts'
