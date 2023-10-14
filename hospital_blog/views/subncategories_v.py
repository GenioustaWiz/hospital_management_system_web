
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib import messages

from ..models.categories_n_babies_m import *
from ..forms.category_n_babies_f import *
from taggit.models import Tag

from ..models.article_m import Blog
from ..models.categories_n_babies_m import Category

# This one shows all subcategories and Blogs Under the Clicked Category
def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    subcategories = Subcategory.objects.filter(category=category)
    blogs = Blog.objects.filter(category=category,status=Blog.PUBLISHED, hidden=False, approved=True).order_by('-date_published')
    # Query the database for the most recent articles
    recent_articles = Blog.objects.filter(category=category,status=Blog.PUBLISHED, hidden=False, approved=True).order_by('-date_created')[:5]
    categories = Category.objects.filter(approved=True)
    # Get all available tags
    all_tags = Tag.objects.all()
    context = {
        'category': category,
        'subcategories': subcategories,
        'blogs': blogs,
        'categories': subcategories,
        'recent_articles': recent_articles,
        'all_tags': all_tags,  # Add this line to the context
    }
    return render(request, 'blog/category/category_detail.html', context)
# End of Category_details

# This one shows all subcategories and Blogs Under the Clicked Category
def subcategory_detail(request, slug):
    subcategory = get_object_or_404(Subcategory, slug=slug)
    categories = Category.objects.filter(approved=True)
    blogs = Blog.objects.filter(subcategory=subcategory,status=Blog.PUBLISHED, hidden=False, approved=True).order_by('-date_published')
    # Query the database for the most recent articles
    recent_articles = Blog.objects.filter(subcategory=subcategory, status=Blog.PUBLISHED, hidden=False, approved=True).order_by('-date_created')[:5]
    categories = Category.objects.filter(approved=True)
    # Get all available tags
    all_tags = Tag.objects.all()
    context = {
        'subcategory': subcategory,
        'blogs': blogs,
        'categories': categories,
        'recent_articles': recent_articles,
        'all_tags': all_tags,  # Add this line to the context
    }
    return render(request, 'blog/subcategory/subcategory_detail.html', context)

# End of Subcategory_details