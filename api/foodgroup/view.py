from rest_framework import viewsets

from api.foodgroup import serializers
from core.models import FoodGroup


class FoodGroupViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        return FoodGroup.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return serializers.FoodGroupSerializerList
        if self.action == "retrieve":
            return serializers.FoodGroupSerializerDetail
        return serializers.FoodGroupSerializerList
