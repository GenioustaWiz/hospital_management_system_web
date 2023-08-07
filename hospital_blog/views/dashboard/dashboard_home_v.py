

from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.db.models import Sum
from django.contrib import messages

from ...utils.time_since_published import time_since_published


from ...models.article_m import *

@login_required
def dashboard_home(request):
    author = request.user
    
    if author.is_staff:
        # if admin is logged in, show information for all blogs
        blogs_ = Blog.objects.all()
        blogs_c = Blog.objects.all().annotate(total_comments=Sum('comments__approved')) or 0
        if blogs_.exists():
            total_comments = blogs_c.aggregate(Sum('total_comments'))['total_comments__sum'] or 0
            total_views = Blog.objects.aggregate(Sum('view_count'))['view_count__sum'] or 0
        else:
            total_comments=0
            total_views=0
        total_blogs = Blog.objects.count()
        total_published_blogs = Blog.objects.filter(status='PUBLISHED').count() or 0
        recent_blogs  = Blog.objects.filter(status='PUBLISHED', hidden=False).order_by('-date_published')[:5]
        total_rejected = Blog.objects.filter(rejected=True).count() or 0
        total_approved = Blog.objects.filter(approved=True).count() or 0
        total_hidden = Blog.objects.filter(hidden=True).count() or 0
        messages.success(request, 'This is a success message.')
    else: 
        # for normal authors, show information for their own blogs only
        blogs_ = Blog.objects.all()
        blogs_c = Blog.objects.filter(author=author).annotate(total_comments=Sum('comments__approved')) or 0
        if blogs_.exists():
            total_comments = blogs_c.aggregate(Sum('total_comments'))['total_comments__sum'] or 0
            total_views = Blog.objects.filter(author=author).aggregate(Sum('view_count'))['view_count__sum'] or 0
        else:
            total_comments=0 
            total_views=0
        total_blogs = Blog.objects.filter(author=author).count() or 0
        total_published_blogs = Blog.objects.filter(author=author, status='PUBLISHED').count() or 0
        recent_blogs = Blog.objects.filter(author=author, status='PUBLISHED', hidden=False).order_by('-date_published')[:5]
        total_rejected = Blog.objects.filter(author=author,rejected=True).count() or 0
        total_approved = Blog.objects.filter(author=author,approved=True).count() or 0
        total_hidden = Blog.objects.filter(author=author,hidden=True).count() or 0
        messages.success(request, 'This is a success message.')
    context = {
        'total_blogs': total_blogs,
        'total_published_blogs': total_published_blogs,
        'total_views': total_views,
        'total_comments': total_comments,
        'recent_blogs': recent_blogs,
        'total_rejected': total_rejected,
        'total_approved': total_approved,
        'total_hidden': total_hidden,
        }
    return render(request, 'blogdashboard/dashboard_home.html', context)


# Allow staff members (admin) to access this view
@staff_member_required
def dashboard_home_admin(request):
    return dashboard_home(request)
