from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField

class Profile(models.Model):
    is_staff = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE) # Delete profile when user is deleted
    phone_number = PhoneNumberField()
    country= CountryField(blank=True)
    title = models.CharField(default='This is the default, title change it in profile.', max_length=200, null=True)
    desc_text='Hey, there is a default text description about you that you can change it by clicking "Edit" or going'   
    desc = models.TextField(default=desc_text, max_length=200, null=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    github = models.URLField(default='https://www.github.com/', max_length=1000, null=True, blank=True)
    facebook = models.URLField(default='https://www.facebook.com/', max_length=1000, null=True, blank=True)
    googleplus = models.URLField(default='https://www.google.com/', max_length=1000, null=True, blank=True)
    instagram = models.URLField(default='https://www.instagram.com/', max_length=1000, null=True, blank=True)
    
    def __str__(self):
        return f'{self.user.username} Profile' #show how we want it to be displayed

     # Override the save method of the model
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)


        img = Image.open(self.image.path) # Open image 
        
        # resize image
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size) # Resize image
            img.save(self.image.path) # Save it again and override the larger image

# class SocialMediaLinks(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE) # Delete profile when user is deleted
#     github = models.CharField(default='input you Github link here.', max_length=1000, null=True, blank=True)
#     facebook = models.CharField(default='input you Facebook link here.', max_length=1000, null=True, blank=True)
#     googleplus = models.CharField(default='input you Google+ link here.', max_length=1000, null=True, blank=True)
#     instagram = models.CharField(default='input you Instagram link here.', max_length=1000, null=True, blank=True)
    
#     # Override the save method of the model
#     def save(self, *args, **kwargs):
#         super(SocialMediaLinks, self).save(*args, **kwargs)
