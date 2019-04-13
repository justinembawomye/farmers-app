from .serializers import FarmerSerializer
from rest_framework.generics import ListAPIView, CreateAPIView
from .models import Farmer

class FarmerApi(CreateAPIView):
    serializer_class=FarmerSerializer
    queryset = Farmer.objects.all()
   