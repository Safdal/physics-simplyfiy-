from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib.auth.decorators import login_required

# Public view for posts
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

# Admin-only functionality
@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.save()
        return redirect('post_list')
    return render(request, 'blog/post_edit.html', {'post': post})
