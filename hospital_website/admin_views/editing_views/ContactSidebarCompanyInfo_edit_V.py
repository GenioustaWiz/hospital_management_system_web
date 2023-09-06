from django.shortcuts import render, redirect
from ...models.models import ContactSidebarCompanyInfo
from ...forms.ContactSidebarCompanyInfo_F import ContactSidebarCompanyInfoForm

def edit_company_contact_info(request):
    company_info = ContactSidebarCompanyInfo.objects.first()
    if request.method == 'POST':
        form = ContactSidebarCompanyInfoForm(request.POST, instance=company_info)
        if form.is_valid():
            form.save()
            return redirect('companycontact_info_view')
    else:
        form = ContactSidebarCompanyInfoForm(instance=company_info)
    
    return render(request, 
        'maindashboard/ContactSidebarCompanyInfo/edit_company_contact_info.html',
        {'form': form}
    )

