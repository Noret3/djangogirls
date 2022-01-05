from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, DetailView, CreateView

from .models import Post
from .forms import PostForm
from django.utils import timezone


class PostView(ListView):
    model = Post
    queryset = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'


class CreatePostView(CreateView):
    fields = ['title', 'text']

    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)

    def get_queryset(self):
        return Post.objects.all()

    template_name = 'blog/post_edit.html'
