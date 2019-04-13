from django.urls import path
from rest_framework import views
from .api import FarmerApi

urlpatterns=[
path('api/farmer',FarmerApi.as_view() )
]