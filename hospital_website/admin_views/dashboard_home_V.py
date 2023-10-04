from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.db.models import Sum
from django.contrib import messages

from hospital_blog.models.article_m import *
from visitors_counter.models import Visit
@login_required
def main_dashboard_home(request):
    author = request.user
    
    total_blogs = Blog.objects.count()
    total_visitors, total_visits = Visit.get_total_visitors_and_visits()
    total_published_blogs = Blog.objects.filter(status='PUBLISHED').count() or 0
    
    context = {
        'total_blogs': total_blogs,
        'total_visitors': total_visitors,
        'total_visits': total_visits,
        'total_published_blogs': total_published_blogs,
    }
    return render(request, 'maindashboard/dashboard_home.html', context)
    # Allow staff members (admin) to access this view
@staff_member_required
def dashboard_home_admin(request):
    return main_dashboard_home(request)