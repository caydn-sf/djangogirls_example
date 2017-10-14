from django.shortcuts import render
from blog.models import Post 
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.utils import timezone


def post_list(request):
	posts=Post.objects.all()

	return render(request, 'blog/post_list.html', {'gonderiler': posts})

def post_detail(request, pk):
	posts = Post.objects.get(pk=pk)
	return render(request, 'blog/post_detail.html', {'gonderiler': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
    else:
        form = PostForm()
    if form.is_valid():
            post = form.save(commit=False)
            post.yazar = request.user
            post.yayinlanma_tarihi = timezone.now()
            post.save()
            
    
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.yazar = request.user
            post.yayinlanma_tarihi = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})