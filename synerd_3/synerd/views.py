from django.shortcuts import render
from .forms import LoginForm, RegisterForm, OfficeForm, OfficerForm, OrgForm, OrgMemForm, SubscriberForm 
# Create your views here.

def HomePageView(request):
    return render(request, 'synerd/index.html')

def LoginPageView(request):
    login_form = LoginForm()
    return render(request, 'synerd/login.html', {'login_form': login_form})

def RegistrationPageView(request):
    register_form = RegisterForm()
    return render(request, 'synerd/registration.html', {'register_form': register_form})

def PortalPageView(request):
    office_form = OfficeForm()
    officer_form = OfficerForm()
    org_form = OrgForm()
    org_mem_form = OrgMemForm()
    sub_form = SubscriberForm()
    #return render(request, 'synerd/portal.html')
    return render(request, 'synerd/portal.html', {
        'office_form': office_form,
        'officer_form': officer_form,
	'org_form': org_form,
	'org_mem_form': org_mem_form,
	'sub_form': sub_form,
	
    })

