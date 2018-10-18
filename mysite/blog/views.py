from django.shortcuts import render, get_object_or_404
from .models import Blog


def index(request):
    blogs = Blog.objects.filter(is_published=True)
    context = {'blogs': blogs}
    return render(request, 'blog/index.html', context)


def detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'blog/detail.html', {'blog': blog})
