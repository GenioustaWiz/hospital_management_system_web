
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length=100, null=False)
    email = models.EmailField(null=False)
    phone_number = PhoneNumberField()
    subject = models.CharField(max_length=255, null=False)
    message = models.TextField( max_length=600, null=False)
