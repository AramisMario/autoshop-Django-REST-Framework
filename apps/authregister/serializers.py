from apps.authregister.models import *
from rest_framework import serializers
import hashlib

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ('identificationnumber','firstname','lastname','email','password')


class RecepcionistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receptionist
        fields = ('identificationnumber','firstname','lastname','email','password','socialsecuritynumber')

class MechanicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mechanics
        fields = ('identificationnumber','firstname','lastname','email','password','socialsecuritynumber')
