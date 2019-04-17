from django.urls import path
from rest_framework import views, routers
from .api import (FarmerApi, OfficerApi, DistrictApi, SubCountyApi, FarmersApi, ListFarmersApi)

urlpatterns=[
path('api/add-farmer', FarmerApi.as_view(), name='add-farmer'),
path('api/farmers',FarmerApi.as_view(), name='farmers'),
path('api/farmers/<int:pk>',FarmersApi.as_view(), name='delete-farmers'),
path('api/officer',OfficerApi.as_view(), name='officer'),
path('api/district',DistrictApi.as_view(), name='district'),

# officer endpoints
path('api/officers',OfficerApi.as_view(), name='officer'),
path('api/add-officer',OfficerApi.as_view(), name='add-officer'),
]
