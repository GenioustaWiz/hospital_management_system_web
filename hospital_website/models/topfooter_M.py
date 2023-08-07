
from django.db import models

class TopFooterHeading(models.Model):
    heading = models.CharField(default='default', max_length=100, null=False)

    def save(self, *args, **kwargs):
        super(TopFooterHeading, self).save(*args, **kwargs)

class TopFooterContent(models.Model):
    heading = models.ForeignKey(TopFooterHeading, on_delete=models.CASCADE)
    content = models.CharField(default='default',max_length=200, null=False)
    url = models.CharField(max_length=1000, null=True, blank=True)
    
    def save(self, *args, **kwargs):
        super(TopFooterContent, self).save(*args, **kwargs)
