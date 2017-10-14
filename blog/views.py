from django.shortcuts import render
from blog.models import Post 
from django.shortcuts import render, get_object_or_404


def post_list(request):
	posts=Post.objects.all()

	return render(request, 'blog/post_list.html', {'gonderiler': posts})

def post_detail(request, pk):
	posts = Post.objects.get(pk=pk)
	return render(request, 'blog/post_detail.html', {'gonderiler': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
    

