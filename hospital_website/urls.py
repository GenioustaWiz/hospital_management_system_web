
from django.urls import path
from .views import *
urlpatterns = [
    path('', main_index, name='main_index'),
    # path('projects/', projects, name='projects'),
    path('about/', about, name='about'),
]
from django.urls import path
from .views import *
urlpatterns = [
    path('', main_index, name='main_index'),
    # path('projects/', projects, name='projects'),
    path('about/', about, name='about'),
]