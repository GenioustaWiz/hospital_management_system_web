from django.urls import path
from .views import record_visit

urlpatterns = [
    path('record-visit/', record_visit, name='record-visit'),
]
