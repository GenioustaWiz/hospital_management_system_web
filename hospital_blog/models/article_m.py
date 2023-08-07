
from django.db import models
from django.contrib.auth.models import User
# from django_quill.fields import QuillField
from tinymce.models import HTMLField
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils import timezone
import re
from bs4 import BeautifulSoup
from taggit.managers import TaggableManager

from .categories_n_babies_m import *
# from .comments_m import Comment


class Blog(models.Model):
    # Article status constants
    DRAFTED = "DRAFTED"
    PUBLISHED = "PUBLISHED"

    # CHOICES
    STATUS_CHOICES = (
        (DRAFTED, 'Draft'),
        (PUBLISHED, 'Publish'),
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = HTMLField('Content')
    image = models.ImageField(default='article-default.jpg', upload_to='blog_images')
    image_credit = models.CharField(max_length=200, default='CDTBLOG')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, max_length=255, blank=True, null=True)
    tags = TaggableManager(blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,
                              default='DRAFT')
    
    date_published = models.DateTimeField(blank=True, null=True, editable=False)
    date_created = models.DateTimeField(auto_now_add=True,  editable=False)
    date_updated = models.DateTimeField(blank=True, null=True, editable=False)
    date_drafted = models.DateTimeField(blank=True, null=True, editable=False)
    
    word_count = models.IntegerField(default=0)
    view_count = models.IntegerField(default=0)
    like_count = models.IntegerField(default=0)
    dislike_count = models.IntegerField(default=0)
    # comment_count = models.IntegerField(default=0)
    
    date_hidden = models.DateTimeField(blank=True, null=True,editable=False)
    hidden = models.BooleanField(default=False)
    
    date_approved = models.DateTimeField(blank=True, null=True, editable=False)
    approved = models.BooleanField(default=False)
    
    date_rejected = models.DateTimeField(blank=True, null=True, editable=False)
    rejected = models.BooleanField(default=False)
    rejection_reason = models.TextField(blank=True, null=True)
    

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # word_count = len(re.findall(r'\w+', self.content))
        # self.word_count = word_count
    
        soup = BeautifulSoup(self.content, 'html.parser')
        # remove images
        for img in soup.find_all('img'):
            img.decompose()
        # count words in text
        text = soup.get_text()
        words = re.findall(r'\b\w+\b', text)
        self.word_count = len(words)
        
        if not self.id:
            self.slug = slugify(self.title,)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:blog_detail', args=[str(self.slug)])

    def publish(self):
        self.published_date = timezone.now()
        self.draft = False
        self.save()

    def unpublish(self):
        self.published_date = None
        self.draft = True
        self.save()
        
    def formatted_views_count(self):
        if self.view_count < 1000:
            # If views are less than 1000, display them as-is
            return str(self.view_count)
        elif self.view_count < 1000000:
            # If views are between 1000 and 999,999, display them with a "k" suffix
            return f"{self.view_count // 1000}.{self.view_count % 1000 // 100}k"
        else:
            # If views are over 1 million, display them with an "m" suffix
            return f"{self.view_count // 1000000}.{self.view_count % 1000000 // 100000}m"
        
    def read_time(self):
        words = self.word_count
        if words > 0:
            read_time = round(words / 200)
            if read_time == 0:
                read_time = 1
            
            if read_time >= 60:
                read_time = round(read_time / 60)
                if read_time == 1:
                    return '1 hr'
                else:
                    return f'{read_time} hrs'
            else:
                if read_time == 1:
                    return '1 min'
                else:
                    return f'{read_time} mins'
        else:
            return 0


    def add_like(self):
        self.like_count += 1
        self.save()

    def add_dislike(self):
        self.dislike_count += 1
        self.save()

    def delete_blog(self):
        self.delete()

    @property
    def comment_count(self):
        """ blog=self is not a must """
        count_ =self.comments.filter(blog=self, approved=True).count()
        if count_ >= 1000:
            suffixes = ['', 'k', 'M', 'B', 'T']
            magnitude = 0
            while count_ >= 1000 and magnitude < len(suffixes)-1:
                magnitude += 1
                count_ /= 1000
                _count = f'{count_:.1f}{suffixes[magnitude]}'
            return _count
        else:
            return count_


