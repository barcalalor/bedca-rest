from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from api.food import serializers
from core.models import Food


class FoodViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        return Food.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return serializers.FoodSerializerList
        if self.action == "retrieve":
            return serializers.FoodSerializerDetail
        if self.action == "profile":
            return serializers.FoodSerializerDetail
        return serializers.FoodSerializerList

    @action(detail=True, methods=['GET'])
    def profile(self, request, pk):
        food = Food.objects.get(id=pk)
        serializer = serializers.FoodProfileSerializer(food)
        return Response(serializer.data)

