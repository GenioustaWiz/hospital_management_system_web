from django.db import models
from django.db.models import F
from django.utils import timezone
from django.db.models import Sum, Count

class Visit(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)
    ip_address = models.GenericIPAddressField()
    visit_count = models.PositiveIntegerField(default=1)
    last_visit = models.DateTimeField(default=timezone.now)  # Add this line for last_visit

    def increment_visit_count(self):
        self.visit_count = models.F('visit_count') + 1
        self.save()
    
    @classmethod
    def get_total_visitors_and_visits(cls):
        total_visitors = cls.objects.aggregate(total_visitors=Count('ip_address', distinct=True))
        total_visits = cls.objects.aggregate(total_visits=Sum('visit_count'))
        return total_visitors['total_visitors'], total_visits['total_visits']