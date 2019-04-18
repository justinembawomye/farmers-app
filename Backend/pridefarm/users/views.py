from rest_framework import generics
from rest_framework import viewsets, permissions

from . import models
from . import serializers

class UserListView(generics.ListCreateAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer


class UserApi(generics.RetrieveAPIView):
    permission_classes=[permissions.IsAuthenticated,]
    serializer_class = serializers.UserSerializer

    def get_object(self):
        return self.request.user
