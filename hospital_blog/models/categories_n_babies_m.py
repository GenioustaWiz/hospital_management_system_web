
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, max_length=255, blank=True, null=True)
    image = models.ImageField(default='category-default.jpg', upload_to='category_images',blank=True, null=True)
    approved = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_approved = models.DateTimeField(blank=True, null=True, editable=False)
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('blog:category_detail', args=[str(self.slug)])
        #return reverse('blog:category_detail', kwargs={'slug': Category.slug})
    #For counting the no of blog under the specific category
    def blog_count(self):
        return self.blog_set.filter(status='PUBLISHED', approved=True).count()

class Subcategory(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, max_length=255, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_approved = models.DateTimeField(blank=True, null=True, editable=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('blog:subcategory_detail', args=[str(self.slug)])
    #For counting the no of blog under the specific subcategory
    def blog_count(self):
        return self.blog_set.filter(status='PUBLISHED', approved=True).count()
