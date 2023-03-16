from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import (
    PlayerAttributes, Booster, Procedure, Equipment, Player, 
    OrganDonor, OrganData, OrganRecipient, MedicalStaff, 
    TechnicalStaff, VehicleStorageArea, Vehicle, OrganStorageArea, 
    Clinic, OrganPossessed, Location,
)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ['key']

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'

class PlayerAttributesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerAttributes
        fields = '__all__'

class BoosterSerializer(serializers.ModelSerializer):
    which_improves = PlayerAttributesSerializer(many=True)
    which_worsens = PlayerAttributesSerializer(many=True)
    
    class Meta:
        model = Booster
        fields = '__all__'

class ProcedureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procedure
        fields = '__all__'

class EquipmentSerializer(serializers.ModelSerializer):
    enables_the_procedure = ProcedureSerializer()

    class Meta:
        model = Equipment
        fields = '__all__'

class OrganDonorSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganDonor
        fields = '__all__'

class OrganDataSerializer(serializers.ModelSerializer):
    procedures = serializers.StringRelatedField(many=True)

    class Meta:
        model = OrganData
        fields = '__all__'

class OrganRecipientSerializer(serializers.ModelSerializer):
    organ = OrganDataSerializer()

    class Meta:
        model = OrganRecipient
        fields = '__all__'

class MedicalStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalStaff
        fields = '__all__'

class TechnicalStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnicalStaff
        fields = '__all__'

class VehicleStorageAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleStorageArea
        fields = '__all__'

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

class OrganStorageAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganStorageArea
        fields = '__all__'

class ClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields = '__all__'

class OrganPossessedSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganPossessed
        fields = '__all__'