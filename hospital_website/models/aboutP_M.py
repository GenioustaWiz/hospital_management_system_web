
from django.db import models
from PIL import Image
desc = 'Please write the description here'
class AboutPage(models.Model):
    heading = models.CharField(default='default', max_length=100, null=False)
    body = models.TextField(default=desc, max_length=600, null=False)

    def save(self, *args, **kwargs):
        if AboutPage.objects.count() >= 1:
            existing_about_page = AboutPage.objects.first()
            existing_about_page.heading = self.heading
            existing_about_page.body = self.body
            AboutPage.objects.filter(pk=existing_about_page.pk).update(
                heading=self.heading, body=self.body
            )
        else:
            super(AboutPage, self).save(*args, **kwargs)

class AboutList(models.Model):
    title = models.CharField(default='default', max_length=100, null=False)
    image = models.ImageField(upload_to='hospital_abt_images',)
    related_items = models.ManyToManyField('self', blank=True)
    
    def save(self, *args, **kwargs):
        super(AboutList, self).save(*args, **kwargs)
        
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)