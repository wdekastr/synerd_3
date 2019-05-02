from ..models import Subscriber, Service, Organization, UserInfo
from rest_framework import generics, permissions
from .serializers import SubscriberSerializer, ServiceSerializer, OrganizationSerializer, UserInfoSerializer, UserSerializer, CreateUserInfoSerializer
from rest_framework import filters
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model

class CreateUserView(CreateAPIView):
    model = get_user_model()
    permission_classes = [        
            permissions.AllowAny
            ]
    serializer_class = UserSerializer

class CreateUserInfoView(CreateAPIView):
    model = UserInfo
    permission_classes = [
            permissions.AllowAny
            ]
    serializer_class = CreateUserInfoSerializer

class ServiceListView(generics.ListAPIView): 
    queryset = Service.objects.all() 
    serializer_class = ServiceSerializer

class ServiceDetailView(generics.RetrieveAPIView): 
    queryset = Service.objects.all() 
    serializer_class = ServiceSerializer

class SubscriberListView(generics.ListAPIView): 
    queryset = Subscriber.objects.all() 
    serializer_class = SubscriberSerializer

class SubscriberListView(generics.ListAPIView):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ['subscriberID','username__username', 'servicecode__servicecode', 'subscriptiontypecode__subscriptiontypecode', 'requestdate', 'startdate', 'enddate', 'motifofcancellation']

class SubscriberDetailView(generics.RetrieveAPIView): 
    queryset = Subscriber.objects.all() 
    serializer_class = SubscriberSerializer

class OrganizationListView(generics.ListAPIView): 
    queryset = Organization.objects.all() 
    serializer_class = OrganizationSerializer

class OrganizationDetailView(generics.RetrieveAPIView): 
    queryset = Organization.objects.all() 
    serializer_class = OrganizationSerializer

class UserInfoListView(generics.ListAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username', 'firstname')


