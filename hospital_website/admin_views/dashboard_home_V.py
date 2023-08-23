from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.db.models import Sum
from django.contrib import messages

from hospital_blog.models.article_m import *
@login_required
def main_dashboard_home(request):
    author = request.user
    
    if author.is_staff:
        total_blogs = Blog.objects.count()
    
    context = {
        'total_blogs': total_blogs,
    }
    return render(request, 'maindashboard/dashboard_home.html', context)
    # Allow staff members (admin) to access this view
@staff_member_required
def dashboard_home_admin(request):
    return main_dashboard_home(request)