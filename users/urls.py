from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *


urlpatterns = [
    path('register/', register, name='signup'),
    # path('profile_home/', profile_home, name='profile-home'),
    path('profile/', profile, name='profile'),
    path('login/', Login, name='login'),
    
    # path('login/', auth_views.LoginView(template_name='users/login.html'), name='login'),
    # path('logout/', auth_views.LogoutView(template_name='users/logout.html'), name='logout'),
]