
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib import messages

from ..models.categories_n_babies_m import *
from ..forms.category_n_babies_f import *
from ..models.article_m import * #Imports Blog model

# This one shows all subcategories and Blogs Under the Clicked Category
def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    subcategories = Subcategory.objects.filter(category=category)
    blogs = Blog.objects.filter(category=category, approved=True).order_by('-date_published')
    context = {
        'category': category,
        'subcategories': subcategories,
        'blogs': blogs,
    }
    return render(request, 'blog/category/category_detail.html', context)
# End of Category_details

# This one shows all subcategories and Blogs Under the Clicked Category
def subcategory_detail(request, slug):
    subcategory = get_object_or_404(Subcategory, slug=slug)
    categories = Category.objects.filter(approved=True)
    blogs = Blog.objects.filter(subcategory=subcategory, approved=True).order_by('-date_published')
    context = {
        'categories': categories,
        'blogs': blogs,
    }
    return render(request, 'blog/subcategory/subcategory_detail.html', context)

# End of Subcategory_details