from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from .forms import BlogPostForm

def blog_post_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'myapp/blog_post_list.html', {'posts': posts})

def blog_post_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    return render(request, 'myapp/blog_post_detail.html', {'post': post})

def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_post_list')  # Redirect to the blog post list after saving
    else:
        form = BlogPostForm()

    return render(request, 'myapp/create_blog_post.html', {'form': form})