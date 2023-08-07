
from django.shortcuts import render
from taggit.models import Tag

from ..models.article_m import Blog

def tag_blogs(request, tag_slug):
    tag = Tag.objects.get(slug=tag_slug)
    blogs = Blog.objects.filter(tags=tag)
    context = {'tag': tag, 'blogs': blogs}
    return render(request, 'blog/tags/tag_blogs_list.html', context)
