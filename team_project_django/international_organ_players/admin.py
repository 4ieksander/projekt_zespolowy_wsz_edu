from django.contrib import admin
from .models import OrganDonor, OrganData, OrganRecipient, MedicalStaff, TechnicalStaff, Clinic
# Register your models here.

admin.site.register(OrganDonor)
admin.site.register(OrganData)
admin.site.register(OrganRecipient)
admin.site.register(MedicalStaff)
admin.site.register(TechnicalStaff)
admin.site.register(Clinic)
