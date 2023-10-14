
from django.urls import path, include
from .views.article_v import *
from .views.subncategories_v import *
from .views.dashboard.dashboard_home_v import *
from .views.dashboard.dashboard_article_v import *
from .views.dashboard.dashboard_many_v import *
from .views.dashboard.subncategory_d_v import *
from .views.tags_v import tag_blogs
from .views.dynamic_search_JS_V import *


app_name = 'blog'

urlpatterns = [
    path('articles-available/', blog_home, name='blog_home'),
    path('article view/<slug:slug>/', blog_detail, name='blog_detail'),
    path('category article list/<slug:slug>/', category_detail, name='category_detail'),
    path('subcategory article list/<slug:slug>/', subcategory_detail, name='subcategory_detail'),
    path('artcles/tagged/<slug:tag_slug>/', tag_blogs, name='tag_blogs'),
    
    #Dashboard Views
    # path('<slug:slug>/', article_detail, name='article_detail')
    path('dashboard/', dashboard_home, name='dashboard_home'),
    path('create/', blog_create, name='blog_create'),
    
    #DASHBOARD >>>>>>> : dashboard_article_v.py
    path('articles/<slug:slug>/', das_article_detail, name='das_article_detail'),
    path('edit/<slug:slug>/', blog_edit, name='blog_edit'),
    path('approve/<slug:slug>/', blog_approve, name='blog_approve'),
    path('reject/<slug:slug>/', blog_reject, name='blog_reject'),
    path('hide/<slug:slug>/', blog_hide, name='blog_hide'),
    path('unhide/<slug:slug>/', blog_unhide, name='blog_unhide'),
    path('delete/<slug:slug>/', blog_delete, name='blog_delete'),
    # used when using the id to get the data
    path('get_category_by_subcategory/<int:subcategory_id>/', 
         get_category_by_subcategory, name='get_category_by_subcategory'),
    # -----------------------------------------------------------//
        #   used when using slug to get the data
    # path('get_category_by_subcategory/<slug:subcategory_slug>/', 
    #      get_category_by_subcategory, name='get_category_by_subcategory'),
       #-----------------------------------------------------------------------//
    #-----------END DASHBOARD >>>>>>> : dashboard_article_v.py ------------//
    
    path('category/create/', category_create, name='category_create'),
    path('category/edit/<int:id>/', category_edit, name='category_edit'), #will be usin the id instead of slug
    path('category-list/', category_list, name='category_list'),
    
    path('subcategory/create/', subcategory_create, name='subcategory_create'),
    path('subcategory/edit/<int:id>/', subcategory_edit, name='subcategory_edit'),
    path('subcategory list/', subcategory_list, name='subcategory_list'),
    # dashboard_many_v.py
    path('recent articles/', recent_article_list, name='recent_article_list'),
    path('drafted articles/', drafted_article_list, name='drafted_article_list'),
    path('published articles/', published_article_list, name='published_article_list'),
    path('deleted articles/', hidden_article_list, name='hidden_article_list'),
    path('written articles/', written_article_list, name='written_article_list'),
    path('approved articles/', approved_article_list, name='approved_article_list'),
    path('rejected articles/', rejected_article_list, name='rejected_article_list'),
    
    # Add this URL pattern for search suggestions
    path('open-dropeddown-article/<slug:articleSlug>/', open_dropdown_article, name='open_dropdown_article'),
    path('blog-search-results/', blog_search_results, name='blog_search_results'),
    path('blog_search/ajax_search/', blog_ajax_search, name='blog_ajax_search'),
    
]
