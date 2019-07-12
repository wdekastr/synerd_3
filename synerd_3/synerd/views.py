from django.shortcuts import render, get_object_or_404
from .forms import LoginForm, RegisterForm, OfficeForm, OfficerForm, OrgForm, OrgMemForm, SubscriberForm 
import requests
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from backend.models import Service
from django.core.paginator import Paginator

# Create your views here.

def HomePageView(request):
    return render(request, 'synerd/index.html')

def LoginPageView(request):
    login_form = LoginForm()
    if request.method =='POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['Username']
            password = login_form.cleaned_data['Password']
            user = authenticate(username=username, password=password)
            if user is not None and user.is_staff:
                login(request,user)
                return HttpResponseRedirect('/admin/')

            elif user is not None:
                login(request,user)
                return HttpResponseRedirect('/synerd/')

            else:
                return render(request, 'synerd/login.html', {'login_form': login_form})

        else:
            login_form = LoginForm()


    return render(request, 'synerd/login.html', {'login_form': login_form})

def SearchPageView(request):
    searchResult = {}
    if 'search' in request.GET:
        search = request.GET['search']
        url = 'http://127.0.0.1:8000/api/subscribers/?search=%s' % search
        response = requests.get(url)
        searchResult = response.json()
    return render(request, 'synerd/search.html', {'searchResult': searchResult})

def ServiceView(request):
    ServicesResult = Service.objects.all()
    paginator = Paginator(ServicesResult, 1)

    page = request.GET.get('page')
    services = paginator.get_page(page)
    return render(request, 'synerd/services.html', {'services': services})

def DynamicServiceView(request, code):
    obj = get_object_or_404(Service, servicecode=code)
    context = {
            "service": obj
            }
    return render(request, 'synerd/servicesearch.html', context)

def RegistrationPageView(request):
    register_form = RegisterForm()
    error_text = ['Username Already Exists']
    if request.method =='POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
           username = register_form.cleaned_data['Username']
           password = register_form.cleaned_data['Password']
           firstname = register_form.cleaned_data['First_Name']
           middlename = register_form.cleaned_data['Middle_Name']
           lastname = register_form.cleaned_data['Last_Name']
           address1 = register_form.cleaned_data['Address_Line_1']
           address2 = register_form.cleaned_data['Address_Line_2']
           city = register_form.cleaned_data['City']
           state = register_form.cleaned_data['State']
           zipcode = register_form.cleaned_data['Zip_Code']
           email = register_form.cleaned_data['Email']
           homephone = register_form.cleaned_data['Home_Phone_Number']
           cellphone = register_form.cleaned_data['Cell_Phone_Number']
           dob = register_form.cleaned_data['Date_Of_Birth']

           response = requests.post('http://127.0.0.1:8000/api/register/', data={'username': username, 'password': password})
           if response.status_code == 201:
               response = requests.post('http://127.0.0.1:8000/api/createuserinfo/', data={'username': username, 'firstname': firstname, 'middlename': middlename, 'lastname': lastname, 'address1': address1, 'address2': address2, 'city': city, 'state': state, 'zipcode': zipcode, 'email': email, 'homephone': homephone, 'cellphone': cellphone, 'dob': dob})
               user = authenticate(username=username, password=password)
               login(request,user)
               return HttpResponseRedirect('/synerd/')

           else:
               return render(request, 'synerd/registration.html', {'register_form': register_form, 'error_text': error_text,})

        else:
            error_text.clear()
            error_text = ['Incorrect Date of Birth Format']
            return render(request, 'synerd/registration.html', {'register_form': register_form, 'error_text': error_text,})

    
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

