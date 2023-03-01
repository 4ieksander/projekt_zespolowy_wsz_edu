from django.contrib import admin
from .models import OrganDonor, OrganData, OrganRecipient, MedicalStaff, TechnicalStaff, Clinic, VehicleStorageArea, Vehicle, OrganStorageArea, Player, Equipment, Procedure, Booster, PlayerAttributes, Location, OrganPossessed


admin.site.register(OrganDonor)
admin.site.register(OrganData)
admin.site.register(OrganRecipient)
admin.site.register(MedicalStaff)
admin.site.register(TechnicalStaff)
admin.site.register(Clinic)
admin.site.register(VehicleStorageArea)
admin.site.register(Vehicle)
admin.site.register(OrganStorageArea)
admin.site.register(PlayerAttributes)
admin.site.register(Booster)
admin.site.register(Procedure)
admin.site.register(Equipment)
admin.site.register(Player)
admin.site.register(Location)
admin.site.register(OrganPossessed)