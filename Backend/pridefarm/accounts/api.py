from .serializers import (FarmerSerializer, OfficerSerializer, DistrictSerializer, SubCountySerializer, FarmersSerializer)
from rest_framework.generics import (ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView)
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from .models import Farmer, Officer, District, SubCounty

class FarmerApi(CreateAPIView, ListAPIView):
    serializer_class=FarmerSerializer
    queryset = Farmer.objects.all()

class OfficerApi(CreateAPIView,  ListAPIView):
    serializer_class=OfficerSerializer
    queryset = Officer.objects.all()    

class DistrictApi(CreateAPIView):
    serializer_class=DistrictSerializer
    queryset = District.objects.all()       
   

class SubCountyApi(CreateAPIView):
    serializer_class=SubCountySerializer
    queryset = SubCounty.objects.all()      

class ListFarmersApi(ListAPIView):
    serializer_class = FarmerSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        farmer = self.request.user
        return Farmer.objects.all()   


# RetrieveUpdateDestroyAPIView
class FarmersApi(RetrieveUpdateDestroyAPIView):
    queryset = Farmer.objects.all()
    permission_classes =[permissions.AllowAny]
    serializer_class = FarmersSerializer   

