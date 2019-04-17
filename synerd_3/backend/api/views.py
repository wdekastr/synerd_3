from rest_framework import generics
from ..models import Subscriber, Service, Organization
from .serializers import SubscriberSerializer, ServiceSerializer, OrganizationSerializer

class ServiceListView(generics.ListAPIView): 
    queryset = Service.objects.all() 
    serializer_class = ServiceSerializer

class ServiceDetailView(generics.RetrieveAPIView): 
    queryset = Service.objects.all() 
    serializer_class = ServiceSerializer

class SubscriberListView(generics.ListAPIView): 
    queryset = Subscriber.objects.all() 
    serializer_class = SubscriberSerializer

class SubscriberDetailView(generics.RetrieveAPIView): 
    queryset = Subscriber.objects.all() 
    serializer_class = SubscriberSerializer

class OrganizationListView(generics.ListAPIView): 
    queryset = Organization.objects.all() 
    serializer_class = OrganizationSerializer

class OrganizationDetailView(generics.RetrieveAPIView): 
    queryset = Organization.objects.all() 
    serializer_class = OrganizationSerializer

