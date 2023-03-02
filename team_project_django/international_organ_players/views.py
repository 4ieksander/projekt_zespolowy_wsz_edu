from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import permission_required, login_required, user_passes_test
from django.shortcuts import render, redirect

from .create_random_objects import CreateRandomOrganDonor

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import (
    PlayerAttributes, Booster, Procedure, Equipment, Player, 
    OrganDonor, OrganData, OrganRecipient, MedicalStaff, 
    TechnicalStaff, VehicleStorageArea, Vehicle, OrganStorageArea, 
    Clinic, OrganPossessed, Location,
)
from .serializers import (
    PlayerSerializer, PlayerAttributesSerializer, BoosterSerializer,
    ProcedureSerializer, EquipmentSerializer, OrganDonorSerializer, OrganDataSerializer,
    OrganRecipientSerializer, MedicalStaffSerializer, TechnicalStaffSerializer, 
    VehicleStorageAreaSerializer, VehicleSerializer, LocationSerializer,
    OrganStorageAreaSerializer, ClinicSerializer, OrganPossessedSerializer,
)


class PlayerList(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class PlayerAttributesListCreateView(generics.ListCreateAPIView):
    queryset = PlayerAttributes.objects.all()
    serializer_class = PlayerAttributesSerializer

class PlayerAttributesRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PlayerAttributes.objects.all()
    serializer_class = PlayerAttributesSerializer

class BoosterListCreateView(generics.ListCreateAPIView):
    queryset = Booster.objects.all()
    serializer_class = BoosterSerializer

class BoosterRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booster.objects.all()
    serializer_class = BoosterSerializer   
    
class ProcedureListCreateView(generics.ListCreateAPIView):
    queryset = Procedure.objects.all()
    serializer_class = ProcedureSerializer

class ProcedureRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Procedure.objects.all()
    serializer_class = ProcedureSerializer

class EquipmentListCreateView(generics.ListCreateAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer

class EquipmentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer

class OrganDonorList(generics.ListCreateAPIView):
    queryset = OrganDonor.objects.all()
    serializer_class = OrganDonorSerializer

class OrganDonorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrganDonor.objects.all()
    serializer_class = OrganDonorSerializer

class OrganDataList(generics.ListCreateAPIView):
    queryset = OrganData.objects.all()
    serializer_class = OrganDataSerializer

class OrganDataDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrganData.objects.all()
    serializer_class = OrganDataSerializer

class OrganRecipientList(generics.ListCreateAPIView):
    queryset = OrganRecipient.objects.all()
    serializer_class = OrganRecipientSerializer

class OrganRecipientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrganRecipient.objects.all()
    serializer_class = OrganRecipientSerializer

class MedicalStaffList(generics.ListCreateAPIView):
    queryset = MedicalStaff.objects.all()
    serializer_class = MedicalStaffSerializer

class MedicalStaffDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MedicalStaff.objects.all()
    serializer_class = MedicalStaffSerializer

class TechnicalStaffList(generics.ListCreateAPIView):
    queryset = TechnicalStaff.objects.all()
    serializer_class = TechnicalStaffSerializer

class TechnicalStaffDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TechnicalStaff.objects.all()
    serializer_class = TechnicalStaffSerializer

class VehicleStorageAreaList(generics.ListCreateAPIView):
    queryset = VehicleStorageArea.objects.all()
    serializer_class = VehicleStorageAreaSerializer

class VehicleStorageAreaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = VehicleStorageArea.objects.all()
    serializer_class = VehicleStorageAreaSerializer

class VehicleList(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class VehicleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class LocationList(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class OrganStorageAreaList(generics.ListCreateAPIView):
    queryset = OrganStorageArea.objects.all()
    serializer_class = OrganStorageAreaSerializer

class OrganStorageAreaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrganStorageArea.objects.all()
    serializer_class = OrganStorageAreaSerializer

class ClinicList(generics.ListCreateAPIView):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer

class ClinicDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer

class OrganPossessedList(generics.ListCreateAPIView):
    queryset = OrganPossessed.objects.all()
    serializer_class = OrganPossessedSerializer

class OrganPossessedDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrganPossessed.objects.all()
    serializer_class = OrganPossessedSerializer

@login_required
def create_random_organ_donor(request):
        create_random_organ_donor = CreateRandomOrganDonor()
        create_random_organ_donor.create_random_organ_donor()
        return redirect("../")