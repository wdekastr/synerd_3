from django.urls import path
from . import views
app_name = 'synerd'

urlpatterns = [ 
    path('services/', views.ServiceListView.as_view(), name='services_list'), 
    path('services/<pk>/', views.ServiceDetailView.as_view(), name='services_detail'),
    path('subscribers/', views.SubscriberListView.as_view(), name='subscribers_list'), 
    path('subscribers/<pk>/', views.SubscriberDetailView.as_view(), name='subscribers_detail'),
    path('organizations/', views.OrganizationListView.as_view(), name='organization_list'), 
    path('organizations/<pk>/', views.OrganizationDetailView.as_view(), name='organization_detail'),
    path('userinfo/', views.UserInfoListView.as_view(), name='userinfo_list'), 


]

