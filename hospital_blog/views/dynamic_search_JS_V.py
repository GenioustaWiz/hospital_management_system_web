from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.db.models import Q

from ..models.article_m import Blog
def open_dropdown_article(request, articleSlug):

    # Retrieve the blog based on the bloglug
    article = Blog.objects.get(slug=articleSlug)
    if article: 
        return redirect('blog:blog_detail', slug=articleSlug)
    else:
        # Get the previous URL
        previous_url = request.META.get('HTTP_REFERER')
        # return to the previous Url if available
        return redirect(previous_url)
    
    
def blog_search_results(request): # not used blog_home is being used
    print("am in=======================")
    if request.method == 'GET':
        print(request.GET)
        print("am innn========++++++++++++++++++++++")
        query = request.GET.get('query')
        print(query)
        articles = Blog.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query) | Q(author__username__icontains=query)
        )

        context = {
            'articles': articles,
            'query': query,
        }

        return render(request, 'blog/article/search_results.html', context)

def blog_ajax_search(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        articles = Blog.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query) | Q(author__username__icontains=query)
        )

        response_data = {
            'articles': [
                {
                    'title': article.title,
                    'author': article.author.username,
                    'category': article.category.name,  # Convert Category to a string
                    'slug': article.slug
                }
                for article in articles
            ]
        }

        print("response_data:")
        print(response_data)
        
        return JsonResponse(response_data)
