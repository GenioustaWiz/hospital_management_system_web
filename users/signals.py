from django.db.models.signals import post_save #Import a post_save signal when a user is created
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User # Import the built-in User model, which is a sender
from django.dispatch import receiver # Import the receiver
from django.utils import timezone

from .models import Profile


@receiver(post_save, sender=User) 
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()  

@receiver(post_save, sender=User)
def user_logged_in_or_out(sender, instance, **kwargs):
    # Count active sessions to get the number of logged-in users
    active_sessions = Session.objects.filter(expire_date__gte=timezone.now())
    logged_in_users = User.objects.filter(id__in=active_sessions.values('session_key'))
    
    # Display the number of logged-in users
    print(f"Number of logged-in users: {logged_in_users.count()}")
# Connect the signal
post_save.connect(user_logged_in_or_out, sender=User)