
import asyncio

try:
    from asyncio.windows_events import NULL
except ImportError:
    # Handle non-Windows platform or provide an alternative solution
    pass

from django.db import models
from PIL import Image
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models import F
# Create your models here.
desc = 'Please write the description here'
hpage_heading = 'Welcome to Our Caring Hospital'
hpage_desc = 'At Our Caring Hospital, we are dedicated to providing exceptional medical care with compassion and expertise. Your health and well-being are our top priorities, and we take pride in offering a wide range of medical services to meet all your healthcare needs.'
class HomePage(models.Model):
    heading = models.CharField(default=hpage_heading, max_length=100, null=False)
    body = models.TextField(default=hpage_desc,
                            max_length=600, null=True, blank=True)

    def save(self, *args, **kwargs):
        if HomePage.objects.count() >= 1: # makes sure only one model can be saved
            existing_home_page = HomePage.objects.first()
            existing_home_page.heading = self.heading
            existing_home_page.body = self.body
            HomePage.objects.filter(pk=existing_home_page.pk).update(
                heading=self.heading, body=self.body
            )
        else:
            super(HomePage, self).save(*args, **kwargs)
# class main_page_service_details(models.Model):
#     heading = models.CharField(default='default',max_length=100, null=False)
#     body = models.TextField(default='desc', max_length=600, null=False)
#     color = models.CharField(default='green',max_length=100, null=False)
#     image = models.ImageField(default='default_P.png', upload_to='main_page_service_details')
  
#     def save(self, *args, **kwargs):
#         super(main_page_service_details, self).save(*args, **kwargs)


#         img = Image.open(self.image.path) # Open image 
        
#         # resize image
#         if img.height > 300 or img.width > 300:
#             output_size = (300, 300)  # w , h
#             img.thumbnail(output_size) # Resize image
#             img.save(self.image.path) # Save it again and override the larger image

class BaseData(models.Model):
    logo_img = models.ImageField(default='default.png', upload_to='company_Logo',null=True, blank=True)
    logo_name = models.CharField(default='Chipped', max_length=100, null=False)
    footer = models.CharField(default='Update Footer ', max_length=100, null=False)
    #impliment the  Singleton pattern
    def save(self, *args, **kwargs):
        if BaseData.objects.count() >= 1:
            existing_data = BaseData.objects.first()
            existing_data.logo_name = self.logo_name
            existing_data.footer = self.footer
            BaseData.objects.filter(pk=existing_data.pk).update(
                logo_img=self.logo_img, logo_name=self.logo_name,
                footer=self.footer,
            )
        else:
            super(BaseData, self).save(*args, **kwargs)

        img = Image.open(self.logo_img.path)
        if img.height > 40 or img.width > 180:
            output_size = (180, 40)
            img.thumbnail(output_size)
            img.save(self.logo_img.path)
            
class ContactSidebarCompanyInfo(models.Model):
    name = models.CharField(max_length=100, null=False)
    phone_number = PhoneNumberField()
    email = models.EmailField(null=False)
    address = models.CharField(max_length=200, null=False)

    def save(self, *args, **kwargs):
        if ContactSidebarCompanyInfo.objects.count() >= 1:
            existing_info = ContactSidebarCompanyInfo.objects.first()
            existing_info.name = self.name
            existing_info.phone_number = self.phone_number
            existing_info.email = self.email
            existing_info.address = self.address
            ContactSidebarCompanyInfo.objects.filter(pk=existing_info.pk).update(
                name=self.name, phone_number=self.phone_number,
                email=self.email,address=self.address,
            )
        else:
            super(ContactSidebarCompanyInfo, self).save(*args, **kwargs)
            
