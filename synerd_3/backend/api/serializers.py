from rest_framework import serializers
from ..models import Subscriber, Service, Organization, UserInfo

class ServiceSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Service
        fields = ['servicecode', 'servicename', 'description', 'premium', 'allocation']

class SubscriberSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Subscriber
        fields = ['subscriberID', 'username', 'subscriptiontypecode', 'servicecode', 'requestdate', 'startdate', 'enddate', 'motifofcancellation', 'beneficiaryID']

class OrganizationSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Organization
        fields = ['organizationcode', 'organizationname', 'description', 'datejoined', 'address1', 'address2', 'city', 'state', 'zipcode', 'phonenumber']

class UserInfoSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = UserInfo
        fields = ['username', 'firstname', 'lastname']


