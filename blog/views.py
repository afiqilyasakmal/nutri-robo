from django.shortcuts import get_object_or_404, redirect, render

from .models import Post
from .models import Comment

from .forms import CommentForm

from django.http import JsonResponse

# Create your views here.

# detail post dan comments
def detail(request, slug):
    post = Post.objects.get(slug=slug)
    comments_count = len(post.comments.all()) + 1
    comments = post.comments.all()

    comment = None
    form = CommentForm()
    # untuk cek apakah form komentar sudah disubmit atau belum
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return JsonResponse({'commenter': comment.name, 'commenter_email': comment.email, 'commenter_message': comment.comment, 'commenter_posted_on': comment.created_at, 'jumlah_komentar': comments_count})
            # return redirect('post_detail', slug=slug)
    else:
        form = CommentForm()

    return render(request, 'blog/detail.html', {'post': post, 'form': form, 'comments': comments})
