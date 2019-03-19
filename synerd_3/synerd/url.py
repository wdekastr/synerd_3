from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
        path('', views.HomePageView, name='home'),
        path('login/', views.LoginPageView, name='login'),
        path('registration/', views.RegistrationPageView, name='registration'),
]