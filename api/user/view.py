from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import UserSerializer
from api.user import serializers
from rest_framework import viewsets

from authentification.models import User
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        return User.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return serializers.UserSerializerList
        if self.action == "retrieve":
            return serializers.UserSerializerDetail
        if self.action == "create":
            return serializers.UserSerializerCreate
        if self.action == 'update':
            return serializers.UserSerializerUpdate
        return serializers.UserSerializerDetail

  