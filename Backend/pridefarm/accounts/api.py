from .serializers import FarmerSerializer, OfficerSerializer, DistrictSerializer, SubCountySerializer
from rest_framework.generics import ListAPIView, CreateAPIView
from .models import Farmer, Officer, District, SubCounty

class FarmerApi(CreateAPIView):
    serializer_class=FarmerSerializer
    queryset = Farmer.objects.all()

class OfficerApi(CreateAPIView):
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