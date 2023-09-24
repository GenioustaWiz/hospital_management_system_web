from django.db import models

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    day = models.CharField(max_length=20)
    time = models.CharField(max_length=20)
    department = models.CharField(max_length=100)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


class ServiceCategory(models.Model):
    category_name = models.CharField(default='Dental Services Cat-', max_length=200, null=False)
    cat_description = models.TextField(
        default='CaT- Lorem ipsum dolor sit amet, consectetur adipisicingpra esentium eveniet eum libero assumenda.',
        null=False
    )
    iconInput = models.CharField(default='<i class="fa-icon fa-solid fa-truck-medical"></i>', max_length=200, null=False)

    def __str__(self):
        return self.category_name

    def save(self, *args, **kwargs):
        super(ServiceCategory, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Perform any necessary cleanup before deleting (if applicable)
        super(ServiceCategory, self).delete(*args, **kwargs)

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
