from django.contrib import admin
from backend.models import *
# Register your models here.

admin.site.register(UserInfo)
admin.site.register(SubscriptionType)
admin.site.register(Service)
admin.site.register(Office)
admin.site.register(Organization)
admin.site.register(TransferredSubscription)
admin.site.register(Subscriber)
admin.site.register(Officer)
admin.site.register(OrganizationMember)
admin.site.site_url = "/synerd"
