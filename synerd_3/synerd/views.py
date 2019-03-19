from django.shortcuts import render

# Create your views here.

def HomePageView(request):
    return render(request, 'synerd/index.html')

def LoginPageView(request):
    return render(request, 'synerd/login.html')

def RegistrationPageView(request):
    return render(request, 'synerd/registration.html')
