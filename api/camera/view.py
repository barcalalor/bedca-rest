from rest_framework import viewsets, status
from rest_framework.response import Response

from api.camera import serializers
from core.models import Camera


class CameraViewSet(viewsets.ModelViewSet):
    

    def get_queryset(self):
        return Camera.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return serializers.CameraSerializerList
        if self.action == "retrieve":
            return serializers.CameraSerializerDetail
        if self.action == "create":
            return serializers.CameraSerializerCreate
        if self.action == 'update':
            return serializers.CameraSerializerUpdate
