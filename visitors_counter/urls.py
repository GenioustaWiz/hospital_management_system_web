from django.urls import path
from .views import record_visit
from .admin_views.visitors_count_views import visit_list

urlpatterns = [
    path('record-visit/', record_visit, name='record_visit'),
    path('visit-list/', visit_list, name='visit_list'),
]
