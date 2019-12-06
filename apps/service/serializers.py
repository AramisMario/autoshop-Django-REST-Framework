from rest_framework import serializers
from apps.authregister.models import Customers
from apps.service.models import *


class VehicleSerializer(serializers.ModelSerializer):
    customers = serializers.PrimaryKeyRelatedField(queryset = Customers.objects.all())
    refvehicle = serializers.PrimaryKeyRelatedField(queryset = Refvehicle.objects.all())
    class Meta:
        model = Vehicles
        fields = ('licenseplate','refvehicle','customers')

    def create(self,validated_data):
        vehicle = Vehicles.objects.create(licenseplate = validated_data["licenseplate"], refvehicle = validated_data["refvehicle"], customers = validated_data["customers"])
        return vehicle
