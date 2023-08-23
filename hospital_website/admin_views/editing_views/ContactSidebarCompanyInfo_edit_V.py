from django.shortcuts import render
from ...models.models import ContactSidebarCompanyInfo
from ...forms.ContactSidebarCompanyInfo_F import ContactSidebarCompanyInfoForm

def edit_company_contact_info(request):
    company_info = ContactSidebarCompanyInfo.objects.first()
    if request.method == 'POST':
        form = ContactSidebarCompanyInfoForm(request.POST, instance=company_info)
        if form.is_valid():
            form.save()
    else:
        form = ContactSidebarCompanyInfoForm(instance=company_info)
    
    return render(request, 
        'maindashboard/ContactSidebarCompanyInfo/edit_company_contact_info.html',
        {'form': form},
    )

