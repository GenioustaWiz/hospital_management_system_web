

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
from hospital_website.models.models import *

from taggit.models import Tag
from django.db.models import Q
def blog_home(request):
    print("am in=======================")
    if request.method == 'GET':
        print(request.GET)
        print("am innn========++++++++++++++++++++++")
        query = request.GET.get('query')
        print(query)
        if query:
            
            blogs = Blog.objects.filter(
                Q(title__icontains=query) | Q(content__icontains=query)| Q(author__username__icontains=query),
                status=Blog.PUBLISHED,
                hidden=False,
                approved=True,
            )
        else:
            # Otherwise, show all published blogs
            blogs = Blog.objects.filter(status=Blog.PUBLISHED, hidden=False, approved=True)

    categories = Category.objects.filter(approved=True)
    # Query the database for the most recent articles
    recent_articles = Blog.objects.filter(status=Blog.PUBLISHED, hidden=False, approved=True).order_by('-date_created')[:5]
    # Get all available tags
    all_tags = Tag.objects.all()

    context = {
        'blogs': blogs,
        'categories': categories,
        'recent_articles': recent_articles,
        'query': query,
        'all_tags': all_tags,  # Add this line to the context
    }
    return render(request, 'blog/article/blog_home.html', context)

def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug, date_published__lte=timezone.now())
    blog.view_count += 1
    blog.save()
    
    author = blog.author
    author_blogs = Blog.objects.filter(author=author).exclude(slug=slug)
    categories = Category.objects.filter(approved=True)
    # Query the database for the most recent articles
    recent_articles = Blog.objects.filter(status=Blog.PUBLISHED, hidden=False, approved=True).order_by('-date_created')[:5]
    comments = blog.comments.filter(active=True)
     # Get all available tags
    all_tags = Tag.objects.all()
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
        'recent_articles': recent_articles,
        'all_tags': all_tags,  # Add this line to the context
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
