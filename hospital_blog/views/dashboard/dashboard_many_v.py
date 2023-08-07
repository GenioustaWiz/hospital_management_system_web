
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from ...models.article_m import *

@login_required
def recent_article_list(request):
    if request.user.is_staff:
        recent_articles = Blog.objects.filter(hidden=False).order_by('-date_created')[:5]
    else:
        # Query the database for the most recent articles
        recent_articles = Blog.objects.filter(author=request.user, hidden=False).order_by('-date_created')[:5]

    # Pass the list of recent articles to the template
    context = {
        'recent_articles': recent_articles,
    }
    return render(request, 'blogdashboard/rec_article_list.html', context)
@login_required
def drafted_article_list(request):
    if request.user.is_staff:
        drafted_articles = Blog.objects.filter(status='DRAFTED', hidden=False).order_by('-date_drafted')
    else: 
        # Get all blog posts by the current user
        drafted_articles = Blog.objects.filter(author=request.user, status='DRAFTED', hidden=False).order_by('-date_drafted')
    context = {
        'drafted_articles': drafted_articles
    }

    return render(request, 'blogdashboard/dra_article_list.html', context)
@login_required
def published_article_list(request):
    if request.user.is_staff:
        pulished_articles = Blog.objects.filter(status='PUBLISHED', hidden=False).order_by('-date_published')
    else:
        # Get all blog posts by the current user
        pulished_articles = Blog.objects.filter(author=request.user, status='PUBLISHED', hidden=False).order_by('-date_published')
    context = {
        'pulished_articles': pulished_articles
    }

    return render(request, 'blogdashboard/pub_article_list.html', context)
@login_required
def hidden_article_list(request):
    if request.user.is_staff:
        hidden_articles = Blog.objects.filter(hidden=True).order_by('-date_hidden')
    else:
        # Get all blog posts by the current user
        hidden_articles = Blog.objects.filter(author=request.user, hidden=True).order_by('-date_hidden')
    context = {
        'hidden_articles': hidden_articles
    }

    return render(request, 'blogdashboard/hid_article_list.html', context)

@login_required
def written_article_list(request):
    status_filter = request.GET.get('status', None)  # Get the selected filter from the query parameters
    print(status_filter)
    if request.user.is_staff:
        written_articles = Blog.objects.all().order_by('-date_created')
    else:
        # Get all blog posts by the current user
        written_articles = Blog.objects.filter(author=request.user).order_by('-date_created')
    
    # Apply the status filter if it is specified
    if status_filter=='approved':
        written_articles = written_articles.filter(approved=True)
    elif status_filter=='rejected':
        written_articles = written_articles.filter(rejected=True)
    elif status_filter=='hidden':
        written_articles = written_articles.filter(hidden=True)
    elif status_filter=='published':
        written_articles = written_articles.filter(status='PUBLISHED')
    elif status_filter=='drafted':
        written_articles = written_articles.filter(status='DRAFTED')
    else:
        None
    context = {
        'written_articles': written_articles,
        'status_filter': status_filter  # Pass the selected filter to the template
    }
    
    return render(request, 'blogdashboard/wri_article_list.html', context)

@login_required
def approved_article_list(request):
    if request.user.is_staff:
        approved_articles = Blog.objects.filter(approved=True).order_by('-date_approved')[:5]
    else:
        # Query the database for the most recent articles
        approved_articles = Blog.objects.filter(author=request.user, approved=True).order_by('-date_approved')[:5]

    # Pass the list of recent articles to the template
    context = {
        'approved_articles': approved_articles,
    }
    return render(request, 'blogdashboard/appr_article_list.html', context)
@login_required
def rejected_article_list(request):
    if request.user.is_staff:
        rejected_articles = Blog.objects.filter(rejected=True).order_by('-date_rejected')[:5]
    else:
        # Query the database for the most recent articles
        rejected_articles = Blog.objects.filter(author=request.user, rejected=True).order_by('-date_rejected')[:5]

    # Pass the list of recent articles to the template
    context = {
        'rejected_articles': rejected_articles,
    }
    return render(request, 'blogdashboard/rejec_article_list.html', context)