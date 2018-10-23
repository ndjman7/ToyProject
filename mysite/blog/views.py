from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from .forms import BlogForm


def index(request):
    blogs = Blog.objects.filter(is_published=True)
    context = {'blogs': blogs}
    return render(request, 'blog/index.html', context)


def detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'blog/detail.html', {'blog': blog})


def create(request):
    if request.method == 'GET':
        form = BlogForm()
        return render(request, 'blog/upload.html', {'form': form})
    elif request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            # blog = Blog(title=form.cleaned_data['title'],
            #             title_description=form.cleaned_data['title_description'],
            #             content=form.cleaned_data['content'],
            #             is_published=form.cleaned_data['is_published'])
            # blog.save()
            blog = form.save(commit=False)
            blog.user = request.user
            blog.save()
            return redirect('blog:detail', blog.pk)
        else:
            return render(request, 'blog/upload.html', {'form': form})

        #title = request.POST['title']

        #title_description = request.POST['title_description']
        #content = request.POST['content']
        #blog = Blog(title=title, title_description=title_description,
        #            content=content)


def edit(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'GET':
        form = BlogForm(instance=blog)
        return render(request, 'blog/upload.html', {'form': form})
    elif request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            blog = form.save()
            return redirect('blog:detail', blog.pk)
        else:
            return render(request, 'blog/upload.html', {'form': form})
