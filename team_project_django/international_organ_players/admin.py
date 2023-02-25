from django.contrib import admin
from .models import OrganDonor, OrganData, OrganRecipient
# Register your models here.

admin.site.register(OrganDonor)
admin.site.register(OrganData)
admin.site.register(OrganRecipient)
