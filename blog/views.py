from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Post
from django.utils import timezone


class PostView(ListView):
    model = Post
    queryset = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    context_object_name = 'posts'


# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'blog/post_detail.html', {'post': post})


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
