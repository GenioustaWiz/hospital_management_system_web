from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, Group
from ..admin_forms.custom_user_assign_form import GroupAssignmentForm
from ..models import Profile

@login_required
#only users authorized to view users profile will get acces to this
@permission_required('auth.view_user', raise_exception=True) 
def user_detail(request, user_id):
    profile = get_object_or_404(Profile, user_id=user_id)
    user = User.objects.get(id=user_id)
     # Combine first name and last name into a "Name" field
    full_name = f"{profile.user.first_name} {profile.user.last_name}" if profile.user.first_name or profile.user.last_name else "None"

    # Create a dictionary to hold the profile data with "None" for empty fields
    profile_data = {
        
        'Title': profile.title,
        'Name': full_name, #profile.user.first_name,
        'Email': profile.user.email,
        'Phone Number': profile.phone_number,
        'Country': profile.country,
        'Description': profile.desc,
        
    }
    # Replace empty fields with "None"
    for key, value in profile_data.items():
        if not value:
            profile_data[key] = "None"
    if request.method == 'POST':
        action = request.POST.get('action')
        print('====ACTION====')
        print(action)
        form = GroupAssignmentForm(request.POST,)
        if form.is_valid():
            # action = form.cleaned_data.get('action')
            group = form.cleaned_data.get('group')
            print('====ACTION22====')
            print(action)
            if action == 'save_group':
                user.groups.clear()  # Remove user from all groups
                user.groups.add(group)  # Add the selected group
                return redirect('user_detail', user_id=user.id)
            elif action == 'remove_group':
                user.groups.remove(group)  # Remove the selected group
                return redirect('user_detail', user_id=user.id)
            elif action == 'delete_user':
                # Delete the user and their profile
                user.delete()
                return redirect('user_list')  # Redirect to user list or another page after deletion

    else:
        form = GroupAssignmentForm()
            
    context={
        'profile_data': profile_data,
        'profile': profile,
        'form': form,
        }
    return render(request, 'maindashboard/users_admin/user_detail.html', context)
