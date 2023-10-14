
from django.shortcuts import render
from taggit.models import Tag

from ..models.article_m import Blog
from ..models.categories_n_babies_m import Category

def tag_blogs(request, tag_slug):
    tag = Tag.objects.get(slug=tag_slug)
    blogs = Blog.objects.filter(tags=tag, status=Blog.PUBLISHED, hidden=False, approved=True)
    # Query the database for the most recent articles
    recent_articles = Blog.objects.filter(tags=tag, status=Blog.PUBLISHED, hidden=False, approved=True).order_by('-date_created')[:5]
    categories = Category.objects.filter(approved=True)
    # Get all available tags
    all_tags = Tag.objects.all()
    context = {
        'blogs': blogs,
        'categories': categories,
        'recent_articles': recent_articles,
        'all_tags': all_tags,  # Add this line to the context
        }
    return render(request, 'blog/tags/tag_blogs_list.html', context)
