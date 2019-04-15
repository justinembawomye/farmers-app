from django.urls import path
from rest_framework import views
from .api import FarmerApi, OfficerApi, DistrictApi, SubCountyApi, ListFarmersApi

urlpatterns=[
path('api/farmer',FarmerApi.as_view(), name='farmer'),
path('api/officer',OfficerApi.as_view(), name='officer'),
path('api/district',DistrictApi.as_view(), name='district'),
path('api/subcounty',SubCountyApi.as_view(), name='subcounty'),

path('api/allfarmers',ListFarmersApi.as_view(), name='all-farmers'),
]