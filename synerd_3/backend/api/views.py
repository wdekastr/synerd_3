from ..models import Subscriber, Service, Organization, UserInfo
from rest_framework import generics
from .serializers import SubscriberSerializer, ServiceSerializer, OrganizationSerializer, UserInfoSerializer
from rest_framework import filters

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


