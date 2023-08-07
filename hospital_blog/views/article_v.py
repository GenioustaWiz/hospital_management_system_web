

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages

from ..models.article_m import Blog
from ..models.categories_n_babies_m import Category
# from ..forms.article_f import BlogForm
# from ..models.comments_m import Comment
from ..forms.comments_f import CommentForm

def blog_home(request): #displays List of blogs and category
    blogs = Blog.objects.filter(status=Blog.PUBLISHED, hidden=False, approved=True)
    categories = Category.objects.filter(approved=True)
    content = {
        'blogs': blogs,
        'categories' : categories,
    }
    return render(request, 'blog/article/blog_home.html', content)


def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug, date_published__lte=timezone.now())
    blog.view_count += 1
    blog.save()
    
    author = blog.author
    author_blogs = Blog.objects.filter(author=author).exclude(slug=slug)
    categories = Category.objects.filter(approved=True)
    comments = blog.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.blog = blog
            new_comment.save()
            messages.success(request, 'Your comment was added successfully!')
            return redirect(reverse('blog:blog_detail', kwargs={'slug': blog.slug}))
            # return redirect('blog:blog_detail', slug=blog.slug)
    else:
        comment_form = CommentForm()
    context = {
        'blog': blog,
        'author_blogs': author_blogs,
        'comments': comments, 
        'new_comment': new_comment, 
        'comment_form': comment_form,
        'categories' : categories,
    }
    return render(request, 'blog/article/blog_detail.html', context)



# @login_required
# def comment_approve(request, pk):
#     comment = get_object_or_404(Comment, pk=pk)
#     comment.active = True
#     comment.save()
#     messages.success(request, 'The comment was approved successfully!')
#     return redirect('blog_detail', slug=comment.blog.slug)


# @login_required
# def comment_remove(request, pk):
#     comment = get_object_or_404(Comment, pk=pk)
#     comment.delete()
#     messages.success(request, 'The comment was removed successfully!')
#     return redirect('blog_detail', slug=comment.blog.slug)
