from rest_framework.serializers import ModelSerializer

from .models import Farmer

class FarmerSerializer(ModelSerializer):

    class Meta:
        model = Farmer
        fields= ('name',)