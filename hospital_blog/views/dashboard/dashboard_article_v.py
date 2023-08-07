
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages

from ...models.article_m import *
from ...models.categories_n_babies_m import *
from ...forms.article_f import *


@login_required(login_url='user:Login')
def das_article_detail(request, slug): #displays List of blogs and category
    blog = get_object_or_404(Blog, slug=slug)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.rejection_reason = form.cleaned_data['rejection_reason']
            blog.save()
        return redirect('dashboard:article_detail', slug=slug)
    else:
        form = BlogForm(instance=blog)
    context={
    'blog': blog,
    'form': form,
    }
    return render(request, 'blogdashboard/article_detail.html', context)

@login_required
def blog_create(request):
        
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            status = form.cleaned_data.get('status')
            if status == Blog.DRAFTED:
                blog.date_drafted = timezone.now()
            elif status == Blog.PUBLISHED:
                blog.date_published = timezone.now()
            blog.save()
            form.save_m2m()  # save tags
            messages.success(request, f"{blog.title} was succefully created")
            return redirect(blog.get_absolute_url())
    else:
        form = BlogForm()
        context = {
            'form': form,
            'action': 'create',
        }
        
    return render(request, 'blogdashboard/write_article.html', context)

@login_required
def blog_edit(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    # Clean the tags and convert them to a string
    tags = ", ".join([tag.name for tag in blog.tags.all()])
    form = BlogForm(request.POST or None, request.FILES or None, instance=blog)
    context = {
        'action': 'update',
        'form': form,
        'tags': tags,  # Pass the cleaned tags to the context
    }
    if request.method == 'POST':
        if form.is_valid():
            blog = form.save(commit=False)
            # blog.author = request.user
            status = form.cleaned_data.get('status')
            if status == Blog.DRAFTED:
                blog.date_drafted = timezone.now()
            elif status == Blog.PUBLISHED:
                blog.date_published = timezone.now()
            blog.date_updated = timezone.now()
            blog.save()
            form.save_m2m()  # save tags
            messages.success(request, f"{blog.title} was succefully edited")
            return redirect('blog:das_article_detail', slug=blog.slug)
        else:
            # Form is not valid, display errors
            errors = form.errors
            print(errors)

    return render(request, 'blogdashboard/write_article.html', context)

@login_required
def blog_approve(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    blog.approved = True
    blog.rejected = False
    blog.date_approved = timezone.now()
    blog.save()
    messages.success(request, ' post was approved successfully!')
    return redirect('blog:das_article_detail', slug=blog.slug)
@login_required
def blog_reject(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    blog.rejected = True
    blog.approved = False
    blog.date_rejected = timezone.now()
    blog.save()
    messages.success(request, ' post was rejected successfully!')
    return redirect('blog:rejected_article_list')
@login_required
def blog_hide(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    blog.hidden = True
    blog.date_hidden = timezone.now()
    blog.save()
    messages.success(request, 'Your blog post was hidden successfully!')
    return redirect('blog:hidden_article_list')
@login_required
def blog_delete(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    blog.delete_blog()
    messages.success(request, 'Your blog post was Deleted successfully!')
    return redirect('blog:dashboard_home')

@login_required
def blog_unhide(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    blog.hidden = False
    blog.save()
    messages.success(request, 'Your blog post was restored successfully!')
    return redirect('blog:hidden_article_list')

# For receiving the Subcategory that has been clicked so 
# that it can send back the category responsible for it
# when you change to use id make sure you change the url.py to accomodate that
def get_category_by_subcategory(request, subcategory_id):
    subcategory = Subcategory.objects.get(pk=subcategory_id)
    # subcategory = get_object_or_404(Subcategory, slug=subcategory_slug)
    category = subcategory.category
    #RETURNS THE Id of the category responsible for the subcategory selected
    data = {'category_id': category.id} 
    # --------------- - ----------------#
    #RETURNS THE Slug of the category responsible for the subcategory selected
    # data = {'category_slug': category.slug}
    return JsonResponse(data) 
