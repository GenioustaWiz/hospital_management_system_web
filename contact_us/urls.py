
from django.urls import path
from .views import *

# app_name = "contact_us"

urlpatterns = [
    path('contact', contact, name='contact'),
]