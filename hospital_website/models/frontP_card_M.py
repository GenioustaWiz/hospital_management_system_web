
from django.db import models
from PIL import Image
class FrontPageCard1(models.Model):
    heading = models.CharField(default='Emergency Case', max_length=100, null=False)
    body = models.CharField(default='default',max_length=200, null=False)
    color = models.CharField(default='green',max_length=100, null=False)
    iconInput = models.CharField(default='default',max_length=200, null=False)
  
    def save(self, *args, **kwargs):
        if FrontPageCard1.objects.count() >= 1: # makes sure only one model can be saved
            existing_fp_card1 = FrontPageCard1.objects.first()
            existing_fp_card1.heading = self.heading
            existing_fp_card1.body = self.body
            existing_fp_card1.color = self.color
            existing_fp_card1.iconInput = self.iconInput
            FrontPageCard1.objects.filter(pk=existing_fp_card1.pk).update(
                heading=self.heading, body=self.body, 
                color=self.color,iconInput=self.iconInput,
            )
        else:
            super(FrontPageCard1, self).save(*args, **kwargs)

# class FrontPageCardheadings(models.Model):
#     heading = models.CharField(default='Working Hours', max_length=100, null=False)
#     body = models.CharField(default='default',max_length=200, null=False)
  
#     def save(self, *args, **kwargs):
#         super(FrontPageCard1, self).save(*args, **kwargs)
class WorkingHours(models.Model):
    day = models.CharField(max_length=100)
    hours = models.CharField(max_length=100)
   
    def __str__(self):
        return f"{self.day}: {self.hours}"
    def save(self, *args, **kwargs):
        super(WorkingHours, self).save(*args, **kwargs)

class FrontPageCard3(models.Model):
    heading = models.CharField(default='Clinic Timetable', max_length=100, null=False)
    body = models.CharField(default='default',max_length=200, null=False)
    color = models.CharField(default='green',max_length=100, null=False)
    iconInput = models.CharField(default='default',max_length=200, null=False)
  
    def save(self, *args, **kwargs):
        if FrontPageCard3.objects.count() >= 1: # makes sure only one model can be saved
            existing_fp_card3 = FrontPageCard3.objects.first()
            existing_fp_card3.heading = self.heading
            existing_fp_card3.body = self.body
            existing_fp_card3.color = self.color
            existing_fp_card3.iconInput = self.iconInput
            FrontPageCard3.objects.filter(pk=existing_fp_card3.pk).update(
                heading=self.heading, body=self.body, 
                color=self.color,iconInput=self.iconInput,
            )
        else:
            super(FrontPageCard3, self).save(*args, **kwargs)
