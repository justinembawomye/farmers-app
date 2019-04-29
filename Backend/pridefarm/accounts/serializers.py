from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import Farmer, Officer, District, SubCounty

class FarmerSerializer(ModelSerializer):
    username = serializers.JSONField()
    email = serializers.JSONField()
    village = serializers.JSONField()
    class Meta:
        model = Farmer
        fields= ('username','email', 'village')

class FarmersSerializer(ModelSerializer):

    class Meta:
        model = Farmer
        fields= '__all__'        

class OfficerSerializer(ModelSerializer):
    class Meta:
        model = Officer
        fields = '__all__'

class DistrictSerializer(ModelSerializer):
    class Meta:
        model = District
        fields ='__all__'

class SubCountySerializer(ModelSerializer):
    class Meta:
        model = SubCounty
        fields = '__all__'                   