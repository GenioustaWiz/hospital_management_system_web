from django.shortcuts import render
from ..models import Profile

def user_list(request):
    profiles = Profile.objects.all()
    return render(request, 'maindashboard/users_admin/users_list.html', {'profiles': profiles})
