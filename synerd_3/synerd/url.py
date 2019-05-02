from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
        path('', views.HomePageView, name='home'),
        path('login/', views.LoginPageView, name='login'),
        path('registration/', views.RegistrationPageView, name='registration'),
        path('portal/', views.PortalPageView, name='portal'),
        path('search/', views.SearchPageView, name='search'),
        path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
