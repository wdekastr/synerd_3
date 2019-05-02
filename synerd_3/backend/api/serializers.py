from rest_framework import serializers
from ..models import Subscriber, Service, Organization, UserInfo
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        #try:
            user = UserModel.objects.create(
                username=validated_data['username']
                )
            user.set_password(validated_data['password'])
            user.save()
            return user

        #except Exception as exception:
         #   raise ConflictError({"User": "User Already Exists"})

    class Meta:
        model = UserModel
        fields = ['id', 'username', 'password']

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

class CreateUserInfoSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        userinfo = UserInfo.objects.create(username=validated_data['username'], firstname=validated_data['firstname'], middlename=validated_data['middlename'], lastname=validated_data['lastname'], address1=validated_data['address1'], address2=validated_data['address2'], city=validated_data['city'], state=validated_data['state'], zipcode=validated_data['zipcode'], email=validated_data['email'], homephone=validated_data['homephone'], cellphone=validated_data['cellphone'], dob=validated_data['dob'])
        userinfo.save()
        return userinfo

    class Meta:
        model = UserInfo
        fields = ['username', 'firstname', 'middlename', 'lastname', 'address1', 'address2', 'city', 'state', 'zipcode', 'email', 'homephone', 'cellphone', 'dob']
