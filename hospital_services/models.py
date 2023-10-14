from django.db import models
from django.utils.text import slugify
from phonenumber_field.modelfields import PhoneNumberField

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = PhoneNumberField()
    date = models.DateField()
    time = models.TimeField()
    service = models.ForeignKey('ServiceOffered', on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class ServiceCategory(models.Model):
    category_name = models.CharField(default='Dental Services Cat-', max_length=200, null=False)
    cat_description = models.TextField(
        default='CaT- Lorem ipsum dolor sit amet, consectetur adipisicingpra esentium eveniet eum libero assumenda.',
        null=False
    )
    iconInput = models.CharField(default='<i class="fa-icon fa-solid fa-truck-medical"></i>', max_length=200, null=False)
    slug = models.SlugField(unique=True, blank=True)  # Add a slug field

    def __str__(self):
        return self.category_name

    def save(self, *args, **kwargs):
        # Automatically generate the slug based on the category_name
        if not self.slug:
            self.slug = slugify(self.category_name)
        super(ServiceCategory, self).save(*args, **kwargs)
        
class ServiceOffered(models.Model):
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    service_name = models.CharField(default='Dental Services', max_length=100, null=False)
    description = models.TextField(
        default='Lorem ipsum dolor sit amet, consectetur adipisicingpra esentium eveniet eum libero assumenda.',
        null=False
    )
    def __str__(self):
        return self.service_name

    def save(self, *args, **kwargs):
        super(ServiceOffered, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Perform any necessary cleanup before deleting (if applicable)
        super(ServiceOffered, self).delete(*args, **kwargs)

