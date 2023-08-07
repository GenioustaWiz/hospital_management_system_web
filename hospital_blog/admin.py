
from django.contrib import admin
from .models.article_m import *
from .models.categories_n_babies_m import *
from .models.comments_m import *

# Register your models here.
"""Blog model
"""
def approve_blogs(modeladmin, request, queryset):
    queryset.update(approved=True)
    
approve_blogs.short_description = "Approve selected blogs"

class ArticleAdmin(admin.ModelAdmin):

    list_display = ('category','subcategory', 'title', 'approved','hidden', 'author','date_published', 'status')
    list_filter = ('status','author', 'approved')
    search_fields = ('title', 'body',)
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'date_published'
    ordering = ['status', '-date_created', ]
    readonly_fields = ('view_count', 'word_count', 'read_time', 'like_count', 'dislike_count')
    actions = [approve_blogs]
    

# Registers the article model at the admin backend.
admin.site.register(Blog, ArticleAdmin)

class CategoryAdmin(admin.ModelAdmin):

    list_display = ('name', 'slug', 'image', 'approved')
    list_filter = ('name', 'approved',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['name', ]


# Registers the category model at the admin backend.
admin.site.register(Category, CategoryAdmin)

class SubcategoryAdmin(admin.ModelAdmin):

    list_display = ('name', 'slug', 'category', 'approved')
    list_filter = ('name', 'approved','category',)
    search_fields = ('name','category,')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['name', ]


# Registers the category model at the admin backend.
admin.site.register(Subcategory, SubcategoryAdmin)

class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'email', 'content', 'blog', 'created_date', )
    list_filter = ('created_date', 'name',)
    search_fields = ('name', 'article', 'content')
    date_hierarchy = 'created_date'
    ordering = ['-created_date', ]
    readonly_fields = ('name', 'email', 'content', 'blog', 'created_date', 'active',)


# Registers the comment model at the admin backend.
admin.site.register(Comment, CommentAdmin)