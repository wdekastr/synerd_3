from django.db import models
from django.utils import timezone

# Create your models here.

#class Testing(models.Model):
#    testfield = models.CharField(max_length=50)
#
#    def __str__(self):
#        return "Testing: %s" % (self.testfield)
#

class UserInfo(models.Model):
    username = models.CharField(max_length=50, primary_key=True)
    firstname = models.CharField(max_length=50)
    middlename = models.CharField(max_length=50, null=True, blank=True)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    address1 = models.CharField(max_length=50, null=True, blank=True)
    address2 = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    zipcode = models.CharField(max_length=50, null=True, blank=True)
    employername = models.CharField(max_length=50, null=True, blank=True)


    def __str__(self):
        return "Username: %s, First Name: %s, Middle Name: %s, Last Name: %s, Email: %s, Address1: %s, Address2: %s, City: %s, State: %s, Zipcode: %s, Employer Name: %s" % (self.username, self.firstname, self.middlename, self.lastname, self.email, self.address1, self.address2, self.city, self.state, self.zipcode, self.employername)


class SubscriptionType(models.Model):
    subscriptiontypecode = models.CharField(max_length=50, primary_key=True)
    subscriptiontypename = models.CharField(max_length=50)

    def __str__(self):
        return "Subscription Type Code: %s, Subscription Type Name: %s" % (self.subscriptiontypecode, self.subscriptiontypename)


class Service(models.Model):
    servicecode = models.CharField(max_length=50, primary_key=True)
    servicename = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    premium = models.CharField(max_length=50)
    allocation = models.CharField(max_length=50, null=True, blank=True)

    
    def __str__(self):
        return "Service Code: %s, Service Name: %s, Description: %s, Premium: %s, Allocation: %s" % (self.servicecode, self.servicename, self.description, self.premium, self.allocation)


class Office(models.Model):
    officecode = models.CharField(max_length=50, primary_key=True)
    officename = models.CharField(max_length=50)
    attribution = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return "Office Code: %s, Office Name: %s, Attribution: %s" % (self.officecode, self.officename, self.attribution)


class Organization(models.Model):
    organizationcode = models.CharField(max_length=50, primary_key=True)
    organizationname = models.CharField(max_length=50)
    description = models.TextField()
    datejoined = models.DateTimeField(default=timezone.now, null=True, blank=True)
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50, null=True, blank=True)
    phonenumber = models.CharField(max_length=50)
 

    def __str__(self):
        return "Organization Code: %s, Organization Name: %s, Description: %s, Date Joined: %s, Address1: %s, Address2: %s, City: %s, State: %s, Zipcode: %s, Phonenumber: %s" % (self.organizationcode, self.organizationname, self.description, self.datejoined, self.address1, self.address2, self.city, self.state, self.zipcode, self.phonenumber)


class Subscriber(models.Model):
    subscriberID = models.CharField(max_length=50, primary_key=True)
    username = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    subscriptiontypecode = models.ForeignKey(SubscriptionType, on_delete=models.CASCADE)
    servicecode = models.ForeignKey(Service, on_delete=models.CASCADE)
    requestdate = models.DateField()
    startdate = models.DateField()
    enddate = models.DateField(null=True, blank=True)
    motifofcancellation = models.TextField(null=True, blank=True)
    beneficiaryID = models.ForeignKey('Subscriber', on_delete=models.SET_NULL, null=True, blank=True)
 

    def __str__(self):
        #return "Subscriber ID: %s, Username: %s, Subscription Type Code: %s, Service Code: %s, Request Date: %s, Start Date: %s, End Date: %s, Motif: %s, Beneficiary ID: %s" % (self.subscriberID, self.username, self.subscriptiontypecode, self.servicecode, self.requestdate, self.startdate, self.enddate, self.motifofcancellation, self.beneficiaryID)
        return "Subscriber ID: %s, Username %s" % (self.subscriberID, self.username)


class TransferredSubscription(models.Model):
   transferID = models.CharField(max_length=50, primary_key=True)
   transferfrom = models.CharField(max_length=50)
   transferto = models.CharField(max_length=50)
   requestdate = models.DateField()
   transferdate = models.DateField()
   subscriberID = models.ForeignKey(Subscriber, on_delete=models.CASCADE)

   def __str__(self):
       return "Transfer ID: %s, Transfer From: %s, Transfer To: %s, Request Date: %s, Transfer Date: %s, Subscriber ID: %s" % (self.transferID, self.transferfrom, self.transferto, self.requestdate, self.transferdate, self.subscriberID)


class Officer(models.Model):
   officecode = models.ForeignKey(Office, on_delete=models.CASCADE)
   subscriberID = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
   startdate = models.DateField()
   enddate = models.DateField()

   def __str__(self):
       return "Office Code: %s, Subscriber ID: %s, Start Date: %s, End Date: %s" % (self.officecode, self.subscriberID, self.startdate, self.enddate)


class OrganizationMember(models.Model):
   organizationcode = models.ForeignKey(Organization, on_delete=models.CASCADE)
   subscriberID = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
   startdate = models.DateField()
   enddate = models.DateField(null=True, blank=True)
   nativecountry = models.CharField(max_length=50)
   citizenship = models.CharField(max_length=50)
   is_delegate = models.BooleanField()

   def __str__(self):
       return "Organization Code: %s, Subscriber ID: %s, Start Date: %s, End Date: %s, Native Country: %s, Citizenship: %s, Delegate: %s" % (self.organizationcode, self.subscriberID, self.startdate, self.enddate, self.nativecountry, self.citizenship, self.is_delegate)

