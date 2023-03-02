from django.urls import path

from . import views

from .views import *

app_name = 'cmgt_internal'

urlpatterns = [
    path('players/', PlayerList.as_view(), name='player-list'),
    path('players/<int:pk>/', PlayerDetail.as_view(), name='player-detail'),
    path('player-attributes/', PlayerAttributesListCreateView.as_view(), name='player-attributes-list'),
    path('player-attributes/<int:pk>/', PlayerAttributesRetrieveUpdateDestroyView.as_view(), name='player-attribute-detail'),
    path('boosters/', BoosterListCreateView.as_view(), name='boosters-list'),
    path('boosters/<int:pk>/', BoosterRetrieveUpdateDestroyView.as_view(), name='booster-detail'),
    path('procedures/', views.ProcedureListCreateView.as_view(), name='procedures-list'),
    path('procedures/<int:pk>/', ProcedureRetrieveUpdateDestroyView.as_view(), name='procedure-detail'),
    path('equipment/', EquipmentListCreateView.as_view(), name='equipment-list'),
    path('equipment/<int:pk>/', EquipmentRetrieveUpdateDestroyView.as_view(), name='equipment-detail'),
    path('organdonors/', OrganDonorList.as_view(), name='organdonor-list'),
    path('organdonors/<int:pk>/', OrganDonorDetail.as_view(), name='organdonor-detail'),
    path('organdata/', OrganDataList.as_view(), name='organdata-list'),
    path('organdata/<int:pk>/', OrganDataDetail.as_view(), name='organdata-detail'),
    path('organrecipients/', OrganRecipientList.as_view(), name='organrecipient-list'),
    path('organrecipients/<int:pk>/', OrganRecipientDetail.as_view(), name='organrecipient-detail'),
    path('medicalstaff/', MedicalStaffList.as_view(), name='medicalstaff-list'),
    path('medicalstaff/<int:pk>/', MedicalStaffDetail.as_view(), name='medicalstaff-detail'),
    path('technicalstaff/', TechnicalStaffList.as_view(), name='technicalstaff-list'),
    path('technicalstaff/<int:pk>/', TechnicalStaffDetail.as_view(), name='technicalstaff-detail'),
    path('vehiclestoragearea/', VehicleStorageAreaList.as_view(), name='vehiclestoragearea-list'),
    path('vehiclestoragearea/<int:pk>/', VehicleStorageAreaDetail.as_view(), name='vehiclestoragearea-detail'),
    path('location/', LocationList.as_view(), name='location-list'),
    path('location/<int:pk>/', LocationDetail.as_view(), name='location-detail'),
    path('organstoragearea/', views.OrganStorageAreaList.as_view()),
    path('organstoragearea/<int:pk>/', views.OrganStorageAreaDetail.as_view()),
    path('clinic/', views.ClinicList.as_view()),
    path('clinic/<int:pk>/', views.ClinicDetail.as_view()),
    path('organpossessed/', views.OrganPossessedList.as_view()),
    path('organpossessed/<int:pk>/', views.OrganPossessedDetail.as_view()),
]