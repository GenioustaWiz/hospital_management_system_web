from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *
from .admin_views.custom_user_assign_view_V import *
from .admin_views.users_detail_views import *
from .admin_views.users_list_views import *


urlpatterns = [
    path('register/', register, name='signup'),
    # path('profile_home/', profile_home, name='profile-home'),
    path('profile/', profile, name='profile'),
    path('login/', Login, name='login'),
    
    # ========ADMIN URLS VIEWS=======================
    path('assign_group/<int:user_id>/', assign_user_group, name='assign_user_group'),
    
    path('user-list/', user_list, name='user_list'),
    path('user-detail/<int:user_id>/', user_detail, name='user_detail'),
     
    # path('login/', auth_views.LoginView(template_name='users/login.html'), name='login'),
    # path('logout/', auth_views.LogoutView(template_name='users/logout.html'), name='logout'),
]