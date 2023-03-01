from rest_framework import serializers
from .models import Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ["location_name", "coordinator_x", "coordinator_y"]



